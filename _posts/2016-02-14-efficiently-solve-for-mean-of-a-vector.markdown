---
layout: post
title: Efficiently Solve for Mean of a Vector
date: 2016-02-14T00:00:00-05:00
---

This is a really simple thought, but I have reason to post it.

Recently as I was reviewing for the ACTs, one of the simpler questions involved solving for a mean of a set of numbers by hand, formally, an an n-tuple $x=(x_1,...,x_i,...,x_n)$. This question is low hanging fruit, and involves little thinking, so I took a moment to consider how to most efficiently calculate the mean the given set of numbers.

I could have impulsively used brute force to calculate the mean as it is formally defined as:

$$\frac{\sum_{i=0}^n{x_i}}{n}$$

But I know this method takes more time as the numbers get larger.

Instead, we I used this formula:

$$\textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n}$$

The proof for  $$\textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n}=\frac{\sum_{i=0}^n{x_i}}{n}$$ is exceedingly simple:

$$\begin{align}
   \textbf{x}_{min}+\frac{\sum_{i=0}^n{\textbf{x}_i-\textbf{x}_{min}}}{n} \tag 1\\
   = \frac{n\textbf{x}_{min}}{n}+\frac{\sum_{i=0}^n{\textbf{x}_i}}{n}-\frac{nx_{min}}{n} \tag 2\\
   = \frac{\sum_{i=0}^n{\textbf{x}_i}}{n}\tag 3\\
\end{align}$$

You may be laughing at how trivial this concept is, and I agree. My true intent was not to make your life easier by presenting a new way to calculate the mean by hand because you would just use a computer. Instead,  it was an exercise in learning more latex and in simplifying expressions in summation notation.
