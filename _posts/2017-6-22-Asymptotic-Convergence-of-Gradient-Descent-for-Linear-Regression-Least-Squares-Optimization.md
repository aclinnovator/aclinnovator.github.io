---
title: Asymptotic Convergence of Gradient Descent for Linear Regression Least Squares Optimization
author: Akiva Lipshitz
date: June 22, 2017
---



One of the greatest developments in early modern applied mathematics is that of gradient descent, which is a technique for solving programs of the form
$$
\arg\max _x f(x)
$$
by solving a dynamical system 
$$
\mathbf{w}_{t+1} := \mathbf{w}+\lambda(\mathbf{w}\mid \mathbf{x}, \mathbf{y})
$$
Despite its widespread use, the author fears the common user of gradient descent may be unaware of the more nuanced details of its implementation. It is important that they understand its quirks both for their own successful use of the algorithm as well as to ensure their successful automous use and development of new and more learning algorithms. In particular, we show in the case of a simple least-squares linear regression optimization that equation (2) diverges if the learning rate exceeds some given upper bound. We also derive an explicit formula for this upper bound. That such results may be theoretically derived is an innovation in the toolkit used by those who develop and study learning algorithms. It shows that after learning rules have been derived, additional analysis must be performed to understand the asymptotic behavior and stability dynamics of the dynamical system defined by the learning rules. 

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

If $\alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} + 1 \le 1$ then $-1 \le\alpha\frac{\mathbf{x_i}\cdot\mathbf{x_i}}{N} \le 0$. Thus $-1 \le  \frac{\alpha}{N}|\mathbf{x}|^2 \le 0$. This leads to the bounds
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
Equation (12) could have been recognized as a geometric series and is not rewritten as such:
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