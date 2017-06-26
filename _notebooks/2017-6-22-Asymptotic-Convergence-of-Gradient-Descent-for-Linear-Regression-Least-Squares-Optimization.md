---
title: A Bifurcation Point in the Learning Dynamics of Gradient Descent in Linear Least Squares Regression 
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
Observe in this linear task the dynamics of each weight $w_i$ is independent of that of any other weight. We can simplify equation (2) by writing $\beta_ {i1}= - \alpha\mathbf{x_i}\cdot\mathbf{y}\frac{1}{N}$ and $\beta_{i2}=\alpha\mathbf{x}_i \cdot\mathbf{x}_i\frac{1}{N}$, such that 
$$
\Delta w_{i,t} = \beta_{i1}+\beta_{i2}w_{it}
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
Both terms in (8) converge if $-1 < \beta_{i2}+1 < 1$. Recalling from before $\beta_{i2} =\alpha\mathbf{x_i}\cdot\mathbf{x_i}\frac{1}{N}$, 
$$
\begin{align}
-1 < &\beta_{i2}+1  <1 \\
-1 < &\alpha\frac{\|\mathbf{x}\|^2}{N} + 1 < 1 \\
\end{align}
$$
There are two cases to consider and we now go through them:

If 

$$
0 \le \alpha\frac{\|\mathbf{x}\|^2}{N} + 1 < 1
$$
then 

$$
-1 \le \alpha\frac{\|\mathbf{x}\|^2}{N} < 0
$$
Thus 

$$
-1 \le  \frac{\alpha}{N}|\mathbf{x}|^2 < 0
$$
This leads to the bounds
$$
-\frac{N}{\|\mathbf{x}\|^2} \le \alpha< 0
$$
The second case to consider is that of $-1 < \alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} + 1 \le 0$. Here, using a similar thought process
$$
-2\frac{N}{\|\mathbf{x}\|^2} < \alpha \le -\frac{N}{\|\mathbf{x}\|^2}
$$
We now take the union of the sets defined by (17) and (18) as valid $\alpha$ values, naming it $A$. $A$ is expressed in terms of its components because the inner bound is actually significant as it is the *optimal* $\alpha$ value that leads to convergence in one step. 
$$
A_i = \left( -2\frac{N}{\|\mathbf{x}_i\|^2},  -\frac{N}{\|\mathbf{x}\|^2}\right] \cup \left[-\frac{N}{\|\mathbf{x}_i\|^2}, 0 \right)
$$
## A Closed Form Expression

Equation (12) could have been recognized as a geometric series and is now rewritten as such:
$$
w_{it} = (\beta_{i2}+1)^t w_0+ \beta_{i1}\frac{1-(\beta_{i2}+1)^{t}}{\beta_{i2}}
$$
Substitute $\beta$ values  and with some algebra we arrive at the promised closed form expression. That such an equation exists is a rarity. As such, the author believes equation (24) ought to be handled with utmost care and placed deep in a Gringots vault for safekeeping, far from the prying eyes of those nasty adversarial networks. 
$$
w_{it} = \left[\alpha\frac{\|\mathbf{x}_i\|^2}{N} + 1\right]^t w_0-\left[\frac{\mathbf{x_i}\cdot\mathbf{y}}{\|\mathbf{x}_i\|^2} \right]\left[1-\left(\alpha\frac{\|\mathbf{x}_i\|^2}{N} + 1\right)^t\right]
$$
It is now clear to see if $\alpha \not\in A$ then (24) diverges. 

We have tested these results in python simulations and have found that indeed with $\alpha$ values above the upper bound $\alpha \le -\frac{N}{\mathbf{x}_i\cdot\mathbf{x_i}}$ , the system converges, and the opposite for  $\alpha  > -\frac{N}{\| \mathbf{x}_i\|^2}$. 

## The Dynamics of the Learning Process

Having obtain a nice analytical expression for valid $\alpha$ values, we would like to understand the  actual learning dynamics.How is asymptotic convergence affected by the choice of $\alpha$? What is the value of the limit in equation (14)? 

There are a few interesting initial observations to make.

1. From equation (4), we can easily see that if $\hat{y}_j = y_j$ then $\Delta w_{i,t}$. Thus the true solution is a stable point regardless of $\alpha$. 
2. Equation (20) is either monotonically increasing or decreasing. In the limit $t \to \pm\infty$, all lower order terms drop out and the rate of convergence is of the order $\mathcal{O}(\alpha^t)$.
3. We can then write the characteristic timescale of convergence $\tau = \frac{1}{\alpha^t}$ which is exponentially small. Thus we will observe very fast convergence. 

It is worthwhile as an exercise to study the dynamics of the learning system under the extremal values of $\alpha$. 

1. $\alpha = 0$, *stable*. In this case, the weights should diverge linearly. However, because $\beta_{i,1}$ depends on $\alpha$ and $\beta_{i1}$ is also the constant multiple in the geometric series, the sum itself vanishes and the trajectory is stationary. 

2. $\alpha = -\frac{N}{\|\mathbf{x}_i\|^2}$, *stable*. Plugging this into (24) yields an expression 
   $$
   w_t = 0^t\left(w_0 + \frac{\mathbf{x}_i\cdot\mathbf{y}}{\|\mathbf{x}_i\|^2}\right)+\frac{\mathbf{x}_i\cdot\mathbf{y}}{\|\mathbf{x}_i\|^2}
   $$
   This is actually interesting because the system converges in one iteration. The first term vanishes for $t>0$, such that the closed form solution is $\frac{\mathbf{x}_i\cdot\mathbf{y}}{\|\mathbf{x}_i\|^2}$

3. $\alpha = -2\frac{N}{\|\mathbf{x}_i\|^2}$, *unstable*.By plugging in this value of $\alpha$, we get a divergent oscillator. This is effectively a damped oscillator if viewed backwards in time.
   $$
   w_t =(-1)^t w_0 + \frac{\mathbf{x}_i \cdot \mathbf{y}}{\|\mathbf{x}_i\|^2}\left((-2)^t -1\right)
   $$
   By neglecting the terms with constant magnitude, we can rewrite (26) to emphasize its nature as a divergent oscillator. If we look back  at our work, (26) oscillates only because gradient descent looks for the direction of descent, which is the negative of the error gradient with respect to weights. 
   $$
   w_t =  \frac{\mathbf{x}_i \cdot \mathbf{y}}{\|\mathbf{x}_i\|^2}e^{t \ln 2}e^{ i\pi t}
   $$


## Dynamical Bifurcations

At this point we have identified some significant $\alpha$ values and studied the dynamics of the system under such values. To review, we observed stationary dynamics for $\alpha=0$, logistic growth or decay for $\alpha = -N/{\| x \|^2}$, and oscillatory divergence for  $\alpha = -2N/{\|x\|^2}$. Now, notice our equations are continuous for all values of $\alpha$. Thus, with equation (24) we can continuously interpolate between these the distinct dynamical regimes. 

The boundary points of the set $A$ are dynamical bifurcation points. Suppose the boundary points of $A$ are used to dissect the real line into disjoint subsets. The qualitative behavior of learning dynamics is distinct for values of $\alpha$ picked from each of these subsets. 

## Conclusion

We have derived exact analytical bounds on $\alpha$ values which lead to learning convergence. Although linear regression has a closed form solution, that such results exist is exciting. Secondly, auxilary calculations reveal exponentially small convergence timescales. It shows that understanding the learning behavior of gradient descent dynamical systems is actually quite a tractable problem. This ought to inspire efforts to understand the learning process of more complex optimization tasks. This is practically useful as with deeper understanding comes more powerful algorithms. In the longer run, it will be extremely valuable to the effort to decipher the fundamental algorithms underlying intelligent, learning, systems. 