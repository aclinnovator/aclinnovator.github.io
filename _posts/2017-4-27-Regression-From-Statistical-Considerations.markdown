---
layout: post
author: Akiva Lipshitz
date: April 28 2017
title: Theoretical Derivation of Linear Regression From Probabalistic Considerations
---
Consider some set of points $\{(x_i, y_i)\}$ . To make statistically
significant predictions of $y$ given $x$, we would like to learn the
distribution $P(y|x, \mu_ {y(x)},\sigma)$. In this article, we will
derive an algorithm to learn the $y$ for the case when
$\mu_y \propto x$. Specifically, we make the following assumptions

(1) For all $x$, $\sigma_x = \sigma$ where $\sigma$ is some constant
(2) The datapoints are drawn iid from the gaussian distribution
    $\mathcal{N}(y|x,\mu_{y(x)}, \sigma)$

**Define**:

$\hat{y}$ is a single prediction

$\mathbf{\hat{y}}$ is a vector of predictions

$\mathbf{y}$ is a vector of iid draws from 
$\mathcal{P}(y\mid x, \mu_{y(x)}, \sigma_x)$

$\mathbf{x}$ is a vector of $x$ values corresponding to the iid
    draws in $\mathbf{y}$

$\mu_i = \mathbf{y}_i$

We assume that the observed values of $\mathbf{y}$ are the true mean for each $P(y\mid x,\mu_{y(x)}\sigma)$

Recalling the definition of independence

$$\mathcal{P}(x_1, x_2, …, x_n) = \prod \mathcal{P}(x_i)$$

define the
likelyhood function for $\mathbf{\hat{y}}$,

$$\mathcal{L}(\mathbf{y} | \mu, \sigma) = \prod_{i=0}^{N}\mathcal{N}(\hat{y}_i| \mu_i, \sigma)$$

which is a measure of the likelyhood that, given mean $\mu_i$ and
$\sigma$ our predictions will actually be observed and not merely
predicted.

Our problem is reduced to finding those $\mu_i$ and $\sigma$ which
maximize $\mathcal{L}$. Because $\ln x$ is monotonically increasing,
maximizing $\mathcal{L}$ is equivalent to maximizing $\ln \mathcal{L}$.

Then

$$\ln \mathcal{L} = \sum_{i=0}^N\ln\mathcal{N}(\hat{y}_i|\mu_i,\sigma)$$

Recall the definition of the gaussian:

$$\mathcal{N}(x; \mu, \sigma) = \frac{1}{(2\pi \sigma^2)^{1/2}}\exp\left \{ -\frac{1}{2\sigma^2}(x - \mu_x)^2\right \}$$

which we substitute into the log likelyhood function 

$$\begin{aligned}
\ln \mathcal{L} &= \sum_{i=}^N \ln \left( \frac{1}{(2\pi \sigma^2)^{1/2}}\exp\left \{ -\frac{1}{2\sigma^2}(\hat{y}_i^2 - y_i)^2 \right \}\right)\\
& = \sum_{i=0}^N \ln\frac{1}{(2\pi\sigma^2)^{1/2}} -\frac{1}{2\sigma^2}(\hat{y}_i^2 - y_i)^2\\
&= N\ln\frac{1}{(2\pi\sigma^2)^{1/2}}-\frac{1}{2\sigma^2}\sum_{i=0}^N (\hat{y}_i^2 - y_i)^2\\
&= N\ln1- N\ln{2\pi} -\frac{N}{2}\ln\sigma^2-\frac{1}{2\sigma^2}\sum_{i=0}^N (\hat{y}_i^2 - y_i)^2\\
&= - N\ln{2\pi} -\frac{N}{2}\ln\sigma^2e-\frac{1}{2\sigma^2}\sum_{i=0}^N (\hat{y}_i^2 - y_i)^2\\
\end{aligned}$$

I will make a comment about something you may have noticed. This model
assumes that variance is constant with respect to $x$ and that only
$\mu_y$ changes, but never variance.

Now we will make the linearity assumption, i.e. that

$$\hat{\mathbf{y}}(x) = \mathbf{w}^T\mathbf{x} $$

So therefore our problem comes to

$$\arg_{\mathbf{w}} \min (\ln \mathcal{L})$$ 

This is exactly the case
when

$$\frac{d \mathcal{L}}{d \mathbf{w}} = \frac{d}{d \mathbf{w}} \ln\mathcal{L} = \frac{d}{d \mathbf{w}} -\frac{1}{2\sigma^2}\sum_{i=0}^N (\hat{y}_i^2 - y_i)^2 = 0$$

Since maximizing $k \ln w$ is equivalent to maximizing $k \ln w $ for
some constant $k$ , we can replace the $-\frac{1}{2\sigma^2}$ term with
a $\frac{1}{2}$ term instead which simplifies our theoretical
derivations.

The problem as stated mathematically could be solved analytically.
However, that is usually very difficult so we use numerical methods
instead. A common numerical method is gradient descent.

$$\frac{\partial \mathcal{L}}{\partial w_i} = \frac{\partial }{\partial w_i} \left[\frac{1}{2}\sum_{i=0}^N (\hat{y}_i^2 - y_i)^2  \right] = \sum_{i=0}^N (\hat{y}_i - y_i)\frac{\partial \hat{y}_i}{\partial w_i}$$

We then use this method to update the weights accordingly using some
learning rate.

Once we have the weights we have a way of predicting $u_{y(x)}$ for any
$x$ and our $MSE$ is exactly the variance of $P(y|x)$ . Thus we have
successfully fit the distribution
