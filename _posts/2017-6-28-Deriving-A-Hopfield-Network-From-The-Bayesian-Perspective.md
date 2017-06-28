---
title: Deriving a Hopfield Network from The Bayesian Perspective
author: Akiva Lipshitz
date: June 28, 2017
layout: post
---

Of the many mathematical entities I never understood nor could I foresee the day when I could understand them is Hopfield Networks. Hopfield Networks are models of complex addressable memory. In other words, they are dynamical systems designed to encode $N$ arbitrary strings and then converge to a point of perfect recall of any one of these strings if stimulated with a noisy rendition. This article derives the Hopfield Network from scratch and studies its dynamical properties. Hopfield networks are useful to study for educational experience. Not so much is understanding the particular implementation level details of hopfield networks as important as appreciating the perspectives and analytical decisions made in the process. 

Implementing  *content addressable memory*  as a dynamical systems necessitates an ansatz equation, i.e. some initial symbolic structure to play around with. (As much as the field would like its neuronal models to be structure free, the only way to get there is by making simplifying assumptions and introducing structure.). 

Let there be $N$ unique binary strings of length $T$ indexed by $\mu$,  $\mathbf{x}^\mu$, which are observed with some bits randomly flipped. The observation is sampled (1) from the uniform distribution over binary strings, and then this string is permuted by sampling from the distribution over noise. The statistics of noise can be quantified by saying that a single bit $X_t$ is kept with probability $p$ and flipped with probability $1-p$. In particular, let the permutatitive process be interpreted as a random variable $\epsilon$ defined over the sample space $\Omega = \{0, 1\}$. The observed signal is permuted by the noise as follows:

$$
X_t = (1-x_t)\mathcal{E}_t
$$

It follows that $X_t = x_t$ with probability $p$ and $X_t= 1-x_t = \neg x_t$ with probability $1-p$. We will write observations of $X$ as $\tilde{\mathbf{x}}$. 

This statistical backend immediately leads to a quantification of the: what is the true signal that is most likely to have been sampled and then permuted into the observed signal? That is, the goal is to solve 

$$
\arg\max\limits_{\mathbf{x}}\mathcal{P}\left(\mathbf{X}=(1-\mathbf{x})\mathcal{E}\right)
$$

where $\mathbf{X}, \mathbf{x}, \mathbf{\epsilon}$ are vectors. We can assemble a bayesian network from a set of conditionally independent distributions. 

First, we define a uniform distribution over the set of true signals. 

$$
\mathcal{P}(\mathbf{x}) = \frac{1}{N}
$$

Next, we write a distribution for the likelihood of observing any noised signal given the true signal. 

$$
\mathcal{P}(\mathbf{\tilde{x}} \mid \mathbf{x}) =  \alpha^{H_\mu }\beta^{T-H_\mu} \\
$$

where $\alpha =\frac{p}{1-p}$, $\beta = 1-p$  and $H_\mu$ is the number of pairwise different bits between the $\mu$th true signal $\mathbf{x}^\mu$ and the observed signal $\mathbf{\tilde{x}}$, 

$$
H_\mu = \sum\limits_{t=1}^T x_t \wedge\tilde{x}_t
$$

in which  $a \wedge b= a^bb^a = 1-(a+b)+2ab$ is the logical $\text{AND}$ operator, defined for $\{0, 1\}$, which allows $H^\mu$ to be rewritten

$$
H_\mu = \sum\limits_{t=1}^T 1-(\tilde{x}_t+x^\mu_t)+2x^\mu_t\tilde{x}_t
$$

The above two distributions for $\mathcal{P}(\mathbf{x})​$ and $\mathcal{P}(\mathbf{\tilde{x}} \mid \mathbf{x}) ​$ can be combined with Bayes rule to write an expression for total probability of  any observation $\mathbf{\tilde{x}}​$. 

$$
\mathcal{P}(\mathbf{\tilde{x}}) = \sum\limits^N_{\mu=1}\mathcal{P}(\mathbf{\tilde{x}}\mid\mathbf{x}^\mu)\mathcal{P}(\mathbf{x}^\mu)
$$

$$
\mathcal{P}(\mathbf{\tilde{x}}) = \frac{\beta ^T}{N}\sum\limits^N_{\mu=1} \exp\left\{H_\mu\ln\alpha \right\} \\
$$

Then

$$
\frac{\partial \mathcal{P}(\tilde{x}_t)}{\partial\tilde{x}_t} = \frac{\beta^T}{N}\ln\alpha\sum\limits^N_{\mu=1} \exp\left\{H_\mu\ln\alpha \right\} \frac{\partial H_\mu}{\partial \tilde{x}_t}
$$

From (6), 
     
$$
\frac{\partial H^\mu}{\partial \tilde{x}_t} = 2\sum\limits^T_{\mu=1} x^\mu_t-T
$$

This leads directly to the gradient ascent update rule for $\tilde{x}_t$

$$
\tilde{x}_t:= \kappa \sum\limits^N_{\mu=1} \exp\{H_\mu\}
$$

where $\kappa$ is the arbitrarily chosen rate of convergence. 

In the next post, we will study this dynamical system. 



**Bibliography** 

Hancock, Edwin R., and Josef Kittler. "A Bayesian interpretation for the Hopfield network." *Neural Networks, 1993., IEEE International Conference on*. IEEE, 1993.
