---
title: Differential Equations and Modelling of Point Charges
date: 2017-2-2
author: Akiva Lipshitz
layout: post
---

This post continues my [initial thoughts on electrodynamics]({{site.url}}/2017/01/30/The-Electric-Field-Equation.html)

Particles and their dynamics are incredibly fascinating, even wondrous. Give me some particles and some simple equations describing their interactions – some very interesting things can start happening. 

Currently studying electrostatics in my physics class, I am interested in not only the static force and field distributions but also in the dynamics of particles in such fields. To study the dynamics of electric particles is not an easy endeavor – in fact the differential equations governing their dynamics are quite complex and not easily solved manually, especially by someone who lacks a background in differential equations. 

Instead of relying on our analytical abilities, we may rely on our computational abilities and numerically solve the differential equations. Herein I will develop a scheme for computing the dynamics of $n$ electric particles en masse. It will not be computationally easy – the number of operations grows proportionally to $n^2$. For less than $10^4$ you should be able to simulate the particle dynamics for long enough time intervals to be useful. But for something like $10^6$ particles the problem is intractable. You'll need to do more than $10^12$ operations per iteration and a degree in numerical analysis. 



## Governing Equations 

Given $n$ charges $q_1, q_2, ..., q_n$, with masses $m_1, m_2, ..., m_n$ located at positions $\vec{r}_1, \vec{r_2}, ..., \vec{r}_n$, the force induced on $q_i$ by $q_j$ is given by 

$$\vec{F}_{j \to i} = k\frac{q_iq_j}{\left|\vec{r}_i-\vec{r}_j\right|^2}\hat{r}_{ij}$$

where 

$$\hat{r}_{ij} =\frac{ \vec{r}_i-\vec{r}_j}{\left|r_i-r_j\right|}$$

Now, the net *marginal* force on particle $q_i$ is given as the sum of the pairwise forces

$$\vec{F}_{N, i} = \sum_{j \ne i}{\vec{F}_{j \to i}}$$

And then the net acceleration of particle $q_i$ just normalizes the force by the mass of the particle:

$$\ddot{\vec{r}}_i = \frac{\vec{F}_{N, i}}{m_i}$$

In total, for $n$ particles, we have $n$ differential equations. Furthermore, we need to specifiy $n$ initial particle velocities to solve a particular instance of the differential equations. 

To implement this at scale, we're going to need to figure out a scheme for vectorizing all these operations, demonstrated below. 

We'll be using `scipy.integrate.odeint` for our numerical integration. Below, the function `g(y, t, q, m, n, d, k)` is a function that returns the derivatives for all our variables at each iteration. We pass it to `odeint` and then do the integration. 


```python
import numpy as np
import numpy.ma as ma
from scipy.integrate import odeint

def integrator_func(y, t, q, m, n, d, k):
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
        np.power(
            np.sum(np.power(dr, 2), 2)
        ,3./2)
        ,mask=nd_identity)
    # Pairwise q_i*q_j for force equation
    qsa = np.tile(q, (n,1))
    qsb = np.tile(q, (n,1)).T
    qs = qsa*qsb
    # Directional forces
    Fs = (k*qs/drmag).reshape((n,n,1))
    # Dividing by m to obtain acceleration vectors
    a = np.sum(Fs*dr, 1)
    # Setting velocities
    y[:n] = np.copy(y[n:])
    # Entering the acceleration into the velocity slot
    y[n:] = np.copy(a)
    # Flattening it out for scipy.odeint to work
    return np.array(y).reshape(n*2*d)
```

Let's write a general function for simulating particles:

```python
def sim_particles(t, r0, v0, q, m, k=1.):
  	"""
  	With n particles in d dimensions:
  	
  	t: timepoints to integrate over
  	r: n*d matrix. The d-dimensional initial positions of n particles
  	v: n*d matrix of initial particle velocities
  	q: n*1 matrix of particle charges
  	m: n*1 matrix of particle masses
  	k: electric constant.
  	"""
    d = r0.shape[-1]
    n = r0.shape[0]
    y0 = np.zeros((n*2,d))
    y0[:n] = r0
    y0[n:] = v0
    y0 = y0.reshape(n*2*d)
    yf = odeint(
        integrator_func,
        y0,
        t,
        args=(q,m,n,d,k)).reshape(t.shape[0],n*2,d)
    return yf
```

Now, we'll create a timepoint vector to integrate the differential equations over: 


```python
t_f = 10000
t = np.linspace(0, 10, num=t_f)
```

Some other constants


```python
# Number of dimensions
d = 2
# Number of point charges
n = 3
# charge magnitudes, currently all equal to 1
q = np.array([-10,0.2,-5])
# masses
m = np.ones(n)

# The electric constant 
#    k=1/(4*pi*epsilon_naught)
#    Right now we will set it to 1
#    because for our tests we are choosing all q_i =1. 
#    Therefore, k*q is too large a number and causes 
#    roundoff errors in the integrator. 
# In truth:
#    k = 8.99*10**9
# But for now:
k=1.
```

We get to choose the initial positions and velocities of our particles. For our initial tests, we'll set up 3 particles to collide with eachother. 


```python
r1i = np.array([-2., 0.0])
dr1dti = np.array([3.,0.])

r2i = np.array([20.,0.5])
dr2dti = np.array([-3., 0.])

r3i = np.array([11.,20])
dr3dti = np.array([0, -3.])
```

And pack them into an initial state variable we can pass to odeint. 


```python
r0 = np.array([r1i, r2i, r3i])
v0 = np.array([dr1dti, dr2dti, dr3dti])
```

## The Fun Part – Doing the Integration

Now, we'll actually do the integration


```python
# Doing the integration
yf = sim_particles(t, r0, v0, q, m)
```

And finally, we'll plot our results:


```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

fig = plt.figure(figsize=(20,20))
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)
ys1 = yf[:,0,1]
xs1 = yf[:,0,0]

xs2 = yf[:,1,0]
ys2 = yf[:,1,1]

xs3 = yf[:,2,0]
ys3 = yf[:,2,1]

ax.plot(xs1[1], ys1[1],'bv')     
ax.plot(xs1[-1], ys1[-1], 'rv') 

ax.plot(xs2[:1], ys2[:1], 'bv')    
ax.plot(xs2[-1:], ys2[-1:], 'rv') 

ax.plot(xs3[:1], ys3[:1], 'bv')    
ax.plot(xs3[-1:], ys3[-1:], 'rv') 
                                         
ax.plot(xs1, ys1)                      
ax.plot(xs2, ys2)    
ax.plot(xs3, ys3)                      

plt.title("Paths of 3 Colliding Electric Particles")
plt.ion()
plt.show()
```

[Download this post as an ipython notebook](https://gist.github.com/5f52c2bc414a744953e1c69970590f9d)

## Videos
<iframe width="560" height="315" src="https://www.youtube.com/embed/kblQj2h0eJ0" frameborder="0" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/B1RTjIBA6OQ" frameborder="0" allowfullscreen></iframe>
<iframe width="560" height="315" src="https://www.youtube.com/embed/MG-n7eYxbvQ" frameborder="0" allowfullscreen></iframe>

## Path Plot
![png]({{site.url}}/images/electricity_files/electricity_12_0.png)


