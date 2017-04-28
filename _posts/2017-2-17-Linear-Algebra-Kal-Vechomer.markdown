---
title: Basis Vectors and Linear Independence and Learning out Kal Vechomers
author: Akiva Lipshitz
layout: post
---

This post will continue a running theme on my blog, namely showing how mathematical structures provide powerful analogies for conceptually representing and manipulating complex flows of logic in a sugya of Gemara. Here, I want to show that concepts from linear algebra, specifically the notion of linear independence, vector spaces, and bases, offer a useful structural metaphor for studying sequences of kal vechomer limudim in Gemara. 

I'm going to develop the ideas from linear algebra in a more as opposed to less formal manner. This is to maximize the discreteness of my linear algebra metaphor and to minimize how nebulous a concept it is. Were I only to present the abstract concepts of linear algebra and not their formal manifestion my metaphor has no tangible meaning. Only when you see the kinds of algebraic truths and manipulations that linear algebra supports does the true value of the metaphor materialize. 

I hope that these writings serve two purposes (1) exemplify a novel and genuinely beneficial approach to understanding the flow of logic in Gemara, and possibly at a later stage of the theory, understanding disagreements among Rishonim, and (2) show the mathematically who may have previously misappreciated Gemara in favor of mathematics that Gemara too is driven by a very complex, yet mightily elusive and ordered, inner logical structure. 

The wise and experienced ought to comment on this essay, "what you am doing is not Gemara. It's math." I invite this value critique as it could be true and it takes external confirmation to be validated. As a young adult with a still developing self awareness, is that it is simply probabalistic whether my interest in these ideas is genuine or simply reflects some form of inner conflict. But when the dust settles, these ideas add value; if I determine my developing my mathematical approach to Gemara is in any way detrimental to my broader life activities, I am aware I ought to find new avenues to channel my passions in the proper direction. 

## Minimally Formal Introduction to Linear Algebra

Though I've never formally taken linear algebra in school, I read snippets and do exercises from the Gilbert Strang textbook lying on my bookshelf every once in a while; so I have at least a minimal intuition for linear algebra. Linear algebra studies the properties of particularly defined mathematical objects that describe or generate related sets of objects.

​In a more concrete sense, elementary linear algebra's primary focus is on a particular mathematical structure or notation known as a vector. Vectors are basically a collection of mathematical objects indexed by an arbitrary variable, commonly chosen to be $i$. In particular when we say $\mathbf{v}$ is vector, we mean that the letter $\mathbf{v}$ is a symbol, that, when subscripted with $i$, as in $\mathbf{v}_i = k$ refers to a particular scalar value belonging to a collection of values $\mathbf{v}$.Then we can write out the entire $\mathbf{v} = (v_1, v_2, v_3, …., v_n)$.  On a notational note, I'm using boldface to refer to vectors and italics to refer to subscripts of vectors.

> Arbitrary Definitionions of Elementary Vector Operations: 
>
> 1. For any real $c$ and vector $\mathbf{v}$, 
>
>    1. $c\mathbf{v} = (cv_1, cv_2, cv_3, …., cv_n)$
>    2. $c + \mathbf{v} = (c+v_1, c+v_2, c+v_3, …., c+v_n)$
>
> 2. For any two vectors $\mathbf{v}$ and $\mathbf{w}$
>
> 3. We define the dot product of two vectors 
>    $$
>    \mathbf{v} \cdot \mathbf{w} = \sum_{i=1}^nv_i w_i = \mathbf{w} \cdot \mathbf{v}
>    $$
>
>
>

Now we have operations defined on vectors and can ask the question of what we create using these operations. Said more sharply, we can study the properties of the sets of objects that result from applying these operations on vectors of different form. 



For example, let's choose a vector $\mathbf{v} = (1, 2, 3)$  and ask about the structure of the set that results from $c\mathbf{v}$ where $c$ is an arbitrary real valued number. We see the set  $\{ c\mathbf{v} \mid \in \mathbb{R} \} = \{ (c, 2c, 3c) \mid c \in \mathbb{R} \}$ is actually the set of all ones, doubles, and triples of all real numbers. 

Actually, in general $c\mathbf{v}$ is the set of all ordered collections of $c$ multiplied by each $v_i$.  

Similarly, for two vectors $\mathbf{v} = (e^4,\pi,\sqrt2), \mathbf{w} = (w_1, w_2, w_3)$ 
$$
\mathbf{z} = \mathbf{v} + \mathbf{w} = (e^4+w_1,\pi+w_2,\sqrt2 + w_3)
$$
which literally describes a collection of arbitrary vectors $\mathbf{z}$ whose indices are the values of $w_i$ offset by the corresponding values of $v_i$. 

The most logical thing to consider after briefly thinking about these basic linear operations on vectors is to ask about more complex combinations of vectors using these operations. In the most general way, we can take a vector of vectors $\mathbf{A}$, and a vector of real numbers $\mathbf{c}$ and compute the dot product of the two vectors. This is then get the most general combination of $n$ vectors $\mathbf{a}_1 … \mathbf{a}_n$ using the addition and multiplication operators that we have defined above:  
$$
\mathbf{z} = \mathbf{A} \cdot \mathbf{c} = c_1\mathbf{a}_1 + c_2\mathbf{a}_2 + … + c_n\mathbf{a}_n
$$
This form is called the *linear combination* of $n$ vectors and scalars. 

Because you the reader and I the author are curious and inquisitive people, we wonder about the properties of this operation $\mathbf{A} \cdot \mathbf{c}$. 

The dot product of $\mathbf{A}$ and $\mathbf{c}$ certainly generates some new vector, but what are the properties and constraints on this new vector. To do this, we ought to think in general terms; given $n$ vectors what can and can't they describe? Consider, if we have $n$ vectors $\{ \mathbf{a}_i \mid 0 < i  \le n, i \in \mathbb{N} \}$, we'd like to know if a random vector $\mathbf{q}$ can be described as the linear combination of $k \le n$ of these vectors $\mathbf{a}_i$. Well, to answer this problem we can loosely define the notion of a vector space, a set $V$ of vectors closed under finite vector addition and scalar multiplication. $\mathbf{z}$ defines a vector space as the finite sum of vector addition and scalar multiplication. For example:

Let $\mathbf{a} = (1, 2)$ where $c \in \mathbb{R}$. Is $\{ \mathbf{z} = c\mathbf{a} \}$ a vector space? Loosely, yes it is. 

Take $c_1 = k, c_2 = l$.

Then 
$$
\mathbf{z} = k\mathbf{a} + l\mathbf{a} = (k+l, 2(k+l))
$$
And we see that $\mathbf{z}$ is closed under addition and multiplication. 

With this concept of vector spaces, we'd say the set of linear combinations of $n$ vectors $\mathbf{a}_i$ *spans the basis of a vector space*. Anything in this vector space can be described as a linear combination of $\mathbf{a}_i$. Anything that cannot is not a member of this vector space.

We have the theoretical construct of vector spaces for describing the boundaries of linear combinations of vectors. Now another natural question arises: what if one of the vectors $\mathbf{a}_i$ can in fact be expressed as a linear combination of its peers?

In other words, for some particular set of scalar values $\{c\}$ perhaps it can be that 
$$
\mathbf{a}_i = c_1\mathbf{a}_1 + c_2\mathbf{a}_2 +  … + c_{i-1}\mathbf{a}_{i-1} + c_{i+1} \mathbf{a}_{i+1} + … + c_n\mathbf{a}_n
$$
If this is true then anytime your friend gives you a set of vectors $\{\mathbf{a}_i \}$ and asks you to generate all linear combinations described by the vectors in the set, you ought to be tempted to lessen your workload by removing any redundancies in the set – by determining which vectors in it are in fact linear combinations of their peers. 

There is in fact a common technique in linear algebra known as the casting out technique that allows you to remove redundancies in a group of vectors. It is to understand this casting out technique that I have here discussed many concepts in linear algebra. Understanding this casting out technique provides a very powerful structure for interpreting the dynamics of the first daf of Bava Kamma, much stronger than the combinatorics analogy I wrote about last week. 

The casting out technique works as follows:

The linear combination of $n$ vectors 

$$\mathbf{a}_1, \mathbf{a}_2, …, \mathbf{a}_3$$

is

$$
\mathbf{z} = c_1\mathbf{a}_1 + c_2\mathbf{a}_2 + … + c_n\mathbf{a}_n
$$

If we can write

$$
\mathbf{a}_i = s_1\mathbf{a}_1 + s_2\mathbf{a}_2 +  … + s_{i-1}\mathbf{a}_{i-1} + s_{i+1} \mathbf{a}_{i+1} + … + s_n\mathbf{a}_n
$$

Then $\mathbf{z}$ can be rewritten:

$$
\begin{align}
\mathbf{z} &=  
c_1\mathbf{a}_1 + c_2\mathbf{a}_2 + ...  \\
& + s_1\mathbf{a}_1 + s_2\mathbf{a}_2 +  … + s_{i-1}\mathbf{a}_{i-1} + s_{i+1} \mathbf{a}_{i+1} + … + s_n\mathbf{a}_n  \\
& + ... +  c_n\mathbf{a}_n \\
&= (c_1 + s_1)\mathbf{a}_1 + (c_2 + s_2)\mathbf{a}_2 + ... + (c_{i-1} +  s_{i-1}) \mathbf{a}_{i-1}+  (c_{i+1} +  s_{i+1}) \mathbf{a}_{i+1}+ ... + (c_{n} +  s_{n})\mathbf{a}_{n} \\
& = \sum_{j=0, j\not = i} (c_j + s_j)\mathbf{a}_j
\end{align}
$$

We can start looking for this pattern iteratively. 

We initialize with a set containing only $\{a_1\}$ and after each iteration add $\mathbf{a}_{i+1}$

to the set and determine if the $\mathbf{a}_{i+1}$ can be described as a linear combination of the previous, and if so, updating the coefficients appropriately, and eventually stopping at $\mathbf{a}_n$

## Understanding Bava Kamma

With the vector space metaphor currently occupying our *mindspace*, I'd like to revisit the first mishnah in masechet Bava Kamma and model it in terms of vector spaces and basis vectors. 

I'd like to conceptualize the model first and then use to develop a structured mindspace for thinking about certain very particular aspects of the first daf of Bava Kamma. While I realize the linear algebra comes with a lot of baggage, once these ideas become intuitive they are weightless and offer the potential for profound insight to be discovered. 

Imagine we define a vector in a halachic space, such that each vector is of the form: $(\text{property}_A, \text{property}_B, …)$ where each $\text{property}_k \in \{0, 1\}$. 

Say we have some set of halachic object $H$ and each $H_i = (p_a, p_b, p_c, …)$

Now it should be possible that by defining a halachic addition operator on vectors in the halchic vector space as well as scalar multiplication for halachic vectors, we can write new halachic objects as the halachic sum of existing objects, that is (keeping in mind the halachic addition operator is yet to be defined):
$$
\mathbf{h'} = c_1\mathbf{h}_1 + c_2\mathbf{h}_2 +  …
$$
This theoretical halachic models at least approximately matches the talmudic reality on the first daf of Bava Kamma. When we stare at this first mishnah in Bava Kamma for a while we can realize something very profound and implied, alluded to by Rashi and the very logical structural flow of the Mishnah and later Gemara itself.  The Mishnah opens by declaring the existence of 4 avot nezikin. It immediately behooves us to set our minds on the broader thoughtspace attached to this deceptively simple statement of the Gemara. That such discrete categories as 4 avot nezikin exist is no simple matter and must be slowly mentally digested. Even more puzzling are the ideas the Mishna subsequently develops, that is, the mishna is interested in finding implicative relationships among the four categories such that the halachot of one may be learned from the halachot of any of the others. To think that these matters are as particular as they are presented in the Mishna would be to utterly ignore the Mishna's great underlying dynamic. 

Firstly, though we know these categories are written about directly in the pasuk [^1] do not understand how these categories emerged from the pasuk; 

[^ 1]: Shemot 21:28
