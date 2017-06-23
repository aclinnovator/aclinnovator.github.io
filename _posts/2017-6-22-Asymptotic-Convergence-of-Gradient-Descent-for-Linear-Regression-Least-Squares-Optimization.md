---
title: Asymptotic Convergence of Gradient Descent for Linear Regression Least Squares Optimization
author: Akiva Lipshitz
date: June 22, 2017
layout: post
---



Arguably, one of the most powerful developments in early modern applied mathematics is that of gradient descent, which is a technique for solving programs of the form

$$
\arg\max _x f(x)
$$

by solving a dynamical system 

$$
\mathbf{w}_{t+1} := \mathbf{w}+\lambda(\mathbf{w}\mid \mathbf{x}, \mathbf{y})
$$

Despite its widespread use,  the general public may be unaware of the more nuanced details of its implementation. It is important that they understand its quirks both for their own successful use of the algorithm as well as to ensure their successful automous use and development of new and more learning algorithms. In particular, we show in the case of a simple least-squares linear regression optimization that equation (2) diverges if the learning rate exceeds some given upper bound. We also derive an explicit formula for this upper bound. That such results may be theoretically derived is an innovation in the toolkit used by those who develop and study learning algorithms. It shows that after learning rules have been derived, additional analysis must be performed to understand the asymptotic behavior and stability dynamics of the dynamical system defined by the learning rules. 

## Bounds on Learning Rate $\alpha$ for which Learning Converges

Suppose we have already derived the learning rules for a D dimensional regression from the normality assumption. Also, we have removed all constants of proportionality in the learning equations for the sake of simplicity, which doesn't change the asymptotic behavior of learning. 

Let $\alpha$ be a learning rate, $\mathbf{x}$ be a $T$ by $D$ matrix, $\mathbf{y}$ a T by 1 matrix, and $\mathbf{w}$ a D dimensional row vector.

$$
\begin{align}
\Delta w_{i,t} &= -\alpha \sum\limits^N_j (y_i-\hat{y}_j)x_j \\
&= -\alpha \sum\limits^N_j (y_i-w_jx_{ij})x_{ij}\\
&= -\alpha \mathbf{x}_i\cdot\mathbf{y}\frac{1}{N} + w_{i,t}\alpha \mathbf{x}_i\cdot\mathbf{x}_i\frac{1}{N}
\end{align}
$$

Observe in this linear task the dynamics of each weight $w_i$ is independent of that of any other weight. We can simplify equation (2) by writing $\beta_ {i1}= -\alpha\mathbf{x_i}\cdot\mathbf{y}\frac{1}{N}$ and $\beta_{i2}=\alpha\mathbf{x}_i \cdot\mathbf{x}_i\frac{1}{N}$, such that 


$$
\Delta w_{i,t} = \alpha\beta_{i1}+\alpha\beta_{i2}w_{it}
$$

We would like to analyze the asymptotic behavior of this dynamical system and to do so we need an analytical expression for $w_{i,t}$. First, we will produce an update rule

$$
w_{i,t+1} = \beta_{i1}+w_{it} (\beta_{i2}+1)
$$

which we recognize as a one dimensional autoregressive process with an affine term. We can recursively compose equation (5) with itself, using $w_{i,0} \sim \mathcal{N}(\mu, \sigma)$ as initial conditions. This is a bit of a tedious computation that results in a closed form polynomial expression. We simplify the indices in the computation by assuming it holds for all $w_i$. Thus subscripts in the computation on $w$ refer to iterations, with dimension implied. 

$$
\begin{align}
w_{0} &= w_0\\
w_{1} &= \beta_1+w_0(\beta_2+1)  \\
w_2  &= \beta_1+\beta_1(\beta_2+1)+w_0(\beta_2+1)^2\\
w_3 &= \beta_1 + \beta_1(\beta_2+1)+\beta_1(\beta_2+1)^2+w_0(\beta_2+1)^3\\ 
w_n &=w_0(\beta_2 + 1)^n +  \beta_1\sum^{n-1}_{j=0}(\beta_2+1)^j 
\end{align}
$$

This leads to somewhat of a closed form expression:

$$
w_{it} = (\beta_{i2}+1)^t w_{i0}+\beta_{i1}\sum\limits^{t-1}_{j=1}(\beta_{i2}+1)^j
$$

We are interested in the limit $t\to \infty$ as it relates to $\alpha$. 

$$
\lim\limits_{t\to\infty} \left [w_{it} = (\beta_{i2}+1)^t w_{i0}+\beta_{i1}\sum\limits^{t-1}_{j=1}(\beta_{i2}+1)^j \right] =\ ?
$$

Both terms in (8) converge if $-1 \le \beta_{i2}+1 \le 1$. Recalling from before $\beta_{i2} =\alpha\mathbf{x_i}\cdot\mathbf{x_i}\frac{1}{N}$, 

$$
\begin{align}
-1 \le &\beta_{i2}+1  \le 1 \\
-1 \le &\alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} + 1 \le 1 \\
\end{align}
$$

There are two cases to consider and we now go through them:

If 
$$\alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} + 1 \le 1$$

then 

$$-1 \le\alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} \le 0i$$

Thus 

$$-1 \le  \frac{\alpha}{N}|\mathbf{x}|^2 \le 0$$

This leads to the bounds

$$
-\frac{N}{|\mathbf{x}|^2}\le \alpha \le 0
$$

The second case to consider is that of $-1 \le \alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} + 1 \le 0$. Here, using a similar thought process

$$
-2\frac{N}{|\mathbf{x}|^2} \le \alpha \le -1
$$

We now take the intersection of the sets defined by (17) and (18) as valid $\alpha$ values, naming it $A$

$$
A = \left[ -2\frac{N}{|\mathbf{x}|^2},  -1\right] \cap \left[-\frac{N}{|\mathbf{x}|^2}, 0 \right]
$$

Equation (12) could have been recognized as a geometric series and is now rewritten as such:

$$
w_{it} = \beta_{i2}^t w_0+ \beta_{i1}\frac{1-\beta_{i2}^{t+1}}{1-\beta_{i2}}
$$

Substitute $\beta$ values for the promised closed form expression:

$$
w_{it} = \alpha^t\left (\mathbf{x_i}\cdot\mathbf{x_i}\frac{1}{N}\right)^t w_0-\frac{\alpha-\alpha^{t}\left (\mathbf{x_i}\cdot\mathbf{x_i}\frac{1}{N}\right)^{t+1}}{1-\alpha \left (\mathbf{x_i}\cdot\mathbf{x_i}\frac{1}{N}\right)}\left(\mathbf{x_i}\cdot\mathbf{y}\frac{1}{N}\right)
$$

It is now clear to see if $\alpha \not\in A$ then (20) diverges. 

We have tested these results in python simulations and have found that indeed with $\alpha$ values above an upper bound $\alpha \le \frac{N}{\mathbf{x}_i\cdot\mathbf{x_i}}$ , regression diverges, and the opposite of true for $\alpha < \frac{N}{\mathbf{x}_i\cdot\mathbf{x}_i}$. 

## The Dynamics of the Learning Process

Having obtain a nice analytical expression for valid $\alpha$ values, we would like to understand the  actual learning dynamics. Specifically, how is asymptotic convergence affected by the choice of $\alpha$? 

There are a few interesting observations to make. Firstly, equation (20) is monotonically increasing and in the limit all lower order terms drop out and the rate of convergence is of the order $\mathcal{O}(\alpha^t)$. We can then write the characteristic timescale of convergence $\tau = \frac{1}{\alpha^t}$ which is exponentially small. Thus we will observe very fast convergence. 

## Conclusion

We have derived exact analytical bounds on $\alpha$ values which lead to learning convergence. Although linear regression has a closed form solution, that such results exist is exciting. Secondly, auxilary calculations reveal exponentially small convergence timescales. It shows that understanding the learning behavior of gradient descent dynamical systems is actually quite a tractable problem. This ought to inspire efforts to understand the learning process of more complex optimization tasks. This is practically useful as with deeper understanding comes more powerful algorithms. In the longer run, it will be extremely valuable to the effort to decipher the fundamental algorithms underlying intelligent, learning, systems. 
# Supplementary Materials
This code accompanies the paper *Asymptotic Convergence of Gradient Descent for Linear Regression Least Squares Optimization* (Lipshitz, 2017)

## Initialization


```python
from pylab import *
from numpy import random as random
random.seed(1)
N=1000.
w = array([14., 30.]); 
x = zeros((2, int(N))).astype(float32)
x[0,:] = arange(N).astype(float32)
x[1,:] = 1
y = w.dot(x) + random.normal(size=int(N), scale=100.)
```

## Defining Regression 


```python
yh = lambda xs, ws: \
    ws.dot(xs)
    
grad = lambda ys, yhs, xs: \
    (1./xs.shape[1])*sum((yhs-ys)*xs).astype(float32)
    
delta = lambda gs, a: \
    a*gs
    
def regress(y, x, alpha, T=1000):
    wh = random.normal(2, size=2)
    whs = zeros((T, 2))
    whs[0,:] = wh
    for i in xrange(1,T): 
        wh+=delta(grad(y,yh(x,wh), x), alpha)
        whs[i,:] = wh.copy()
    return wh, whs
```


```python
def regrSample(y, x, alpha, T=1000, N=10):
    out = map(
        lambda a: \
        regress(y,x, alpha, T=T), xrange(N)
    )
    trains = array([o[1] for o in out])
    wDist = array([o[0] for o in out])
    
    return wDist, trains

def statsRegr(*args, **kwargs):
    wDist, trains = regrSample(*args, **kwargs)
    return np.mean(trains, axis=0), np.std(trains, axis=0)
```

## Running Regression above and Below the Upper Bound on $\alpha$

The theoretically derived bounds on $\alpha$ are 

$$\alpha \in  \left[ -2\frac{N}{|\mathbf{x}|^2}, -1\right] \cap \left[-\frac{N}{|\mathbf{x}|^2}, 0 \right]$$

Other $\alpha$ values diverge


```python
alphaOver = -10*N/linalg.norm(x[0,:])**2  
alphaUnder = -N/linalg.norm(x[0,:])**2  
muOver, sigOver = statsRegr(y, x, alphaOver, T=T, N=10)
muUnder, sigUnder = statsRegr(y, x, alphaUnder, T=T, N=10)
```


```python
%matplotlib inline
from scipy.stats import norm
import seaborn as sns
fs = 15
t = np.arange(T)
figure(figsize=(10,6))
subplot(2,1,1)
plot(muOver[:,0], 'r:', label='$w_1$')
plot(muOver[:,1], 'b:', label='$w_2$')
fill_between(t, \
             muOver[:,0]+sigOver[:,0], \
             muOver[:,0]-sigOver[:,0], \
             facecolor='red', alpha=0.5)
fill_between(t,\
             muOver[:,1]+sigOver[:,1], \
             muOver[:,1]-sigOver[:,1], \
             facecolor='blue', alpha=0.5)
xlabel("t [Iterations]", fontdict={'fontsize':fs})
yl = ylabel("$w_{i,t}$",fontdict={'fontsize':fs})
yl.set_rotation('horizontal')
title("a = 10sup a")
# title('$a = \frac{N}{\sum x_i^2}$ + 1')

subplot(2,1,2)
plot(muUnder[:,0], 'r:', label='$w_1$')
plot(muUnder[:,1], 'b:', label='$w_2$')
fill_between(t, \
             muUnder[:,0]+sigUnder[:,0],\
             muUnder[:,0]-sigUnder[:,0],\
             facecolor='red', alpha=0.5)
fill_between(t, \
             muUnder[:,1]+sigUnder[:,1],\
             muUnder[:,1]-sigUnder[:,1],\
             facecolor='blue', alpha=0.5)

xlabel("t [Iterations]", fontdict={'fontsize':fs})
yl = ylabel("$w_{i,t}$", fontdict={'fontsize':fs})
yl.set_rotation('horizontal')
plt.title('a = sup a')
# title("$a = 0.06\times\frac{N}{\sum x_i^2}$")
tight_layout()
suptitle(("Learning Dynamics in "
          "Linear Regression Models \n"
          "For Asymptotically Significant Alpha Values"), y=1.08, fontdict={'fontsize':20});

###################################################
figure(figsize=(10,6))
subplot(2,1,1)
mu0 = muUnder[-1,0]
mu1 = muUnder[-1,1]
title("Distribution of Weights for Bounded Model", \
         y=1.08, \
         fontdict={'fontsize':20})

xmin = max(muUnder[-1,0]-3*sigUnder[-1,0], muUnder[-1,1]-3*sigUnder[-1,1])
xmax = min(muUnder[-1,0]+3*sigUnder[-1,0], muUnder[-1,1]+3*sigUnder[-1,1])

x_axis = np.arange(xmin,xmax, 0.001);
plt.plot(x_axis, norm.pdf(x_axis,muUnder[-1,0],sigUnder[-1,0]),'r:');

plt.plot(x_axis, norm.pdf(x_axis,muUnder[-1,1],sigUnder[-1,1]), 'b:');
p, v = yticks()
plt.yticks(p,map(lambda w: round(w, 2),linspace(0, 1, num=len(p))))
subplot(2,1,2)
title("Distribution of Weights for Unbounded Model", \
         y=1.08, \
         fontdict={'fontsize':20})


k=2
idx=argwhere(~np.isnan(muOver[:,0]))[-1]-1
xmin = max(muOver[idx,0]-k*sigOver[idx,0], muOver[idx,1]-k*sigOver[idx,1])
xmax = min(muOver[idx,0]+k*sigOver[idx,0], muOver[idx,1]+k*sigOver[idx,1])
x_axis = np.linspace(xmin,xmax, num=300);

plt.plot(x_axis, \
         norm.pdf(x_axis,muOver[idx,0],sigOver[idx,0]), \
         'r:');


# plt.plot(x_axis, \
#          norm.pdf(x_axis,muOver[idx,1],sigOver[idx,1]), \
#          'b:');

tight_layout()
```


![png]({{site.url}}/images/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_files/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_8_0.png)



![png]({{site.url}}/images/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_files/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_8_1.png)



```python
b = -N/linalg.norm(x[0,:])**2  
```


```python
figure(figsize=(10,10))
subplot(2,1,1)
title("Closed From Expression", fontdict={'fontsize':10})

T = 10000
w0 = random.normal(2, size=2)
ws = np.zeros((T,2))
beta2 = (1/N)*b*x[0,:].dot(x[0,:])+1
beta1 = -(1/N)*b*x[0,:].dot(y)
for t in xrange(1,T+1):
    ws[t-1,0] = w0[0]*beta2**t + beta1*(1-beta2**(t-1))/(1-beta2)
plot(ws[:,0])

subplot(2,1,2)
title("Simulation", fontdict={'fontsize':10})
wh = w0
whs = zeros((T, 2))
whs[0,:] = wh
for i in xrange(1,T): 
    wh+=delta(grad(y,yh(x,wh), x), b)
    whs[i,:] = wh.copy()
plot(whs[:,0])
suptitle(("Asymptotic Behavior "
         "of Closed form and Simulated Learning "), fontdict={"fontsize":20})
```




    <matplotlib.text.Text at 0x12cd85fd0>




![png]({{site.url}}/images/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_files/Asymptotic%20Convergence%20of%20Gradient%20Descent%20for%20Linear%20Regression%20Least%20Squares%20Optimization_10_1.png)



```python

```
