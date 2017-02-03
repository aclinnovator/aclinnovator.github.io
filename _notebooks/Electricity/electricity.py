import numpy as np
import numpy.ma as ma
from scipy.integrate import odeint

import sys
from PyQt4 import QtGui

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Monitor(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.i = 0

        self.x = yf[self.i,:(n),0]
        self.y = yf[self.i,:(n),1]

        self.line = self.ax.scatter(self.x,self.y)

        self.fig.canvas.draw()

        self.timer = self.startTimer(.1)

    def timerEvent(self, evt):
        if self.i == t_f-1: self.i = 0
        # update the height of the bars, one liner is easier
        self.i += 1
        self.x = yf[self.i,:n,0]
        self.y = yf[self.i,:n,1]
        self.ax.cla()

        self.line = self.ax.scatter(self.x,self.y)
        maxx = np.max(self.x) + 20
        minx = np.min(self.x) - 20
        maxy = np.max(self.y) + 20
        miny = np.min(self.y) - 20
        self.ax.set_ylim(ymax=maxy,ymin=miny)
        self.ax.set_xlim(xmin=minx, xmax=maxx)

        self.fig.canvas.draw()
        self.fig.savefig('./video/frame-{}.png'.format(self.i))

mag = lambda r: np.sqrt(np.sum(np.power(r, 2)))

def integrator_func(y, t, q, m, n,d, k):

        y = np.copy(y.reshape((n*2,d)))

        # rj across, ri down
        rs_from = np.tile(y[:n], (n,1,1))

        # ri across, rj down
        rs_to = np.transpose(rs_from, axes=(1,0,2))

        # directional distance between each r_i and r_j
        # dr_ij is the force from j onto i, i.e. r_i - r_j
        dr = rs_to - rs_from

        # Used as a mask
        nd_identity = np.eye(n).reshape((n,n,1))

        # Force magnitudes
        drmag = ma.array(
            np.sqrt(
                np.sum(
                    np.power(dr, 2), 2)),
            mask=nd_identity)

        # Pairwise q_i*q_j for force equation
        qsa = np.tile(q, (n,1))
        qsb = np.tile(q, (n,1)).T
        qs = qsa*qsb

        # Directional forces
        Fs = (qs/np.power(drmag,2)).reshape((n,n,1))

        # Dividing by m to obtain acceleration vectors
        a = np.sum(Fs*dr, 1)

        # Sliding integrated acceleration
        # (i.e. velocity from previous iteration)
        # to the position derivative slot
        y[:n] = np.copy(y[n:])

        # Entering the acceleration into the velocity slot
        y[n:] = np.copy(a)
        # Flattening it out for scipy.odeint to work
        return np.array(y).reshape(n*2*d)

def sim_particles(t, r, v, q, m, k=1.):
    d = r.shape[-1]
    n = r.shape[0]
    y0 = np.zeros((n*2,d))
    y0[:n] = r
    y0[n:] = v
    y0 = y0.reshape(n*2*d)
    yf = odeint(g, y0, t, args=(q,m,n,d,k)).reshape(t.shape[0],n*2,d)
    return yf

t_f = 100
t = np.linspace(0, 10, num=t_f)
r = np.array([
    [0., 0.],
    [20.,0.],
    [10., 3.],
    [7., 20.]
])
v = np.array([
    [0.,10.],
    [0., -10.],
    [0.,0.],
    [4., 5.]
])
q = np.array([
    20.,
    -20., 
    20, 
    -10.])
m = np.ones(n)

yf = sim_particles(t,r,v,q,m)

app = QtGui.QApplication(sys.argv)
w = Monitor()
w.setWindowTitle("Convergence")
w.show()
sys.exit(app.exec_())
