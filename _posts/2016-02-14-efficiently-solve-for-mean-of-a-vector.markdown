---
layout: post
title: Efficiently Solve for Mean of a Vector
date: 2016-02-14T00:00:00-05:00
---

Recently as I was reviewing for the ACTs, one of the easier questions involved solving for a mean of a set of numbers by hand, formally, an an n-tuple $x=(x_1,...,x_i,...,x_n)$. This question is low hanging fruit, and involves little thinking, so I took a moment to consider how to most efficiently calculate the mean the given set of numbers.

A I could have impulsively used brute force to calculate the mean as it is formally defined:

$$\frac{\sum_{i=0}^n{x_i}}{n}$$

But this method takes more time as the numbers get larger and this question shouldn't take longer than a few seconds. 

Instead, I used this formula:

$$\textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n}$$

The proof for  $$\textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n}=\frac{\sum_{i=0}^n{x_i}}{n}$$ is exceedingly simple:

$$\begin{align}
   \textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n} \tag 1\\
   = \frac{n\textbf{x}_{min}}{n}+\frac{\sum_{i=0}^n{\textbf{x}_i}}{n}-\frac{nx_{min}}{n} \tag 2\\
   = \frac{\sum_{i=0}^n{\textbf{x}_i}}{n}\tag 3\\
\end{align}$$

If you are internally laughing at the triviality of this concept, I concur. Do not make a fundamental attribution error by assuming this post belies my ability to do *real math*. 

My true intent in writing this post was to practice my mathjax skills and to share a quick idea I had. If I don't have time to write about deep ideas, at least I will have shared simpler ones because $1>0$
