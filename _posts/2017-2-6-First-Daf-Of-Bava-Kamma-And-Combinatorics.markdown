---
layout: post
author: Akiva Lipshitz
title: Combinatorics to Help Understand the First Daf of Bava Kamma
---

My brother and I just began the first perek of Gemara Bava Kamma. Bava Kamma initializes by listing four instances, which it calls *avot*, for which the halachot of nezikin apply. Rashi[^1] notes the term *avot* , literally translated as *father*, denotes category. The four categories of *nezikin* damages listed by the mishna are learned directly from Parshat Mishpatim. In subsequent dapim, the Gemara will derive the corollories of these overarching *avot nezikin* categories. 

[^1]: Rashi **ארבעה** אבות נזיקין, Bava Kamma 2a

>  **ארבעה** אבות נזיקין 
>
>  1. השור  – Ox
>  2. והבור – Pit
>  3. והמבעה – definition disputed on 3a
>  4. וההבער – Fire

Having defined the total set of *nezikin* categories, the Mishna now is interested in developing the halachot of these categories. Before diving in, the Mishna wants to see if it can draw a limud between any two categories. 

Let the set of nezikin categories be given as 
$$
N = \big \{ \text{shor}, \text{bor}, \text{mivah}, \text{hever}\big \}
$$
If the Mishnah discovers the halachot of at least one category can be derived in terms of the others then the $4$ avot *nezikin* are not independent and will be reduced to at at least $3$ *avot* nezikin and possibly less. The reasons for this being problematic are at once obvious and also probably too deep for me to comprehend.  The mishnah needs to demonstrate all the categories are independent, that is, they are orthogonal (I got this idea from the casting out technique in linear algebra).  

Let's imagine what the space of limudim looks like; we want to try to do a limud from each category to every other category. The limud space is isomorphic to a complete directed graph with $4$ nodes and $c$ edges, where 


$$
c = 2\times \binom{4}{2} = 2\times\frac{4!}{2\times2} = 12
$$
If we allow the graph to be undirected, i.e. the number of comparisons of categories, we have
$$
c^\prime = c/2 = 6
$$
As pointed out by my brother $c$ edges is actually a lower bound on the total number of comparisons the mishnah can attempt. The reason for this is because for each pairing of categories, $N_i$ and $N_j$, there exists multiple dimensions of comparison. Each category has multiple properties, each of which can be compared with all the other properties of another category. 

The Mishnah goes through a number of comparisons between categories to show they are independent. 

> לא הרי השור כהרי המבעה 
>
> (1 comparison)
>
>  ולא הרי המבעה כהרי השור 
>
> (1 comparison)
>
> ולא זה וזה שיש בהן רוח חיים– כהרי האש שאין בו רוח חיים
>
> (2 comparisons)
>
>  ולא זה וזה שדרכן לילך ולהזיק –כהרי הבור שאין דרכו לילך ולהזיק
>
> (3 comparisons)

Summing up the comparisons: 
$$
1 + 1 + 2 + 3 = 7
$$
we wonder why this is so. We expect there to be either $12$ or $6$ comparisons, so what does $7$ mean?

We can account for this if we do a little bit of investigation. Firstly, notice that the *shor* and *mivah* limud is negated in both directions, i.e. both $\text{shor} \to \text{mivah}$ and $\text{mivah} \to \text{shor}$ is negated, and done so without a stated reason. The other possible limudim are negated in one pass, that is, the mishnah doesn't negate both $a\to b$ as well as $b \to a$. Instead, it seems, the Mishnah's latter comparisons are negated simply by conjuring a line of distinction between them, which is sufficient to negate the limud between them in both directions. Thinking about this, we see that in fact the $12$ comparisons we predicted are all negated by the Mishnah. 

In order that we should really understand how this mishnah works from a mechanistic perspective, we need to take the derivative of each of the mishnah's negations. In doing so, three bigger questions come up. 

1. Rashi is curious why the Mishnah doesn't attempt the limud between *shor* and *bor*, which would make sense if the Mishnah is working in sequence? Based on Rashi's answer, it is interesting that the $\text{shor} \to \text{bor}$ limud can be negated in two ways, (1) that *shor* and *bor* are different because the former involves "life" and the latter does not, and (2) because a shor is an animal and directly induces damage, whereas a bor is inanimate and passively induces damage.  One wonders what other comparisons there are to be made between categories and also why the Mishnah chooses the second negation of $\text{shor} \to \text{bor}$ and not the first.
2. Why does the mishnah negate the $\text{shor} \to \text{mivah}$ in both directions, and not give an explicit reason for this rejection, whereas for all the other negations does it give a logical line of distinction. 
3. What substantites these distinctions between categories in the context of undermining a limud. What about these reasons of why the categories of nezikin are different sufficiently undermines the possibility of doing a limud from one to the other?


The methodology used here was to first develop a strong structure of the literal logic used in the Mishnah and then go on to ask questions about the logical structure of the Mishnah. I'll go into more depth on the answers to these questions next week when we'll get to the Gemara. 








