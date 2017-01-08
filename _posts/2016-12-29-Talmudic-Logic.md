---
otherlangs: he
layout: post
author: Akiva Lipshitz
title: A Tool for Developing an Understanding of Nuance and Subtlety in Gemara
---

Ideas from logic and mathematics have the potential to aid in dissecting Gemara and appreciating from a rigorous standpoint its logical structure.  To the student, formal languages can help accelerate the process of appreciating the very deep and nuanced organization of thought in the Gemara. I offer formal languages as a tool for expressing the Gemara's  *shakla vetarya*  to aid in revealing its underlying structure. 

In formal languages, that certain objective rules govern how statements may be manipulated means in a formal system the space of possible and desirable states and their relationships with eachother are easily explored and reasoned about. 

For a simple example: exploring the solution space of $e^x+y = 10$ is very simple. One may initialize x anywhere on the ordered real number field as $x_1$ and then for the solutions begin enumerating the space of $y=10-x$ for $x$.  In contrast, the problem of exploring the space of metaphors to a particular sentence is not well defined; that it is stated in natural language impedes the solution space from being explored in any consistent way.

The power of formal languages also lie in their predictive ability. Once a statement has been made, the laws governing how it behaves under different conditions allow for insight to emerge. For example, given any $f(x_1)=y_1$ and $f(x_2)=y_2$ we can actually predict any $f(x)$ \(assuming $f$ is a linear function\). This, formal languages allow for statements to say implicitly far more than the space they take up. In some instances, new insight emerges from formal statements without authorial intent. For instance, the simplest equation one will learn in an introductory physics course $F = m\ddot{x}$ seems to suggest a very rigid linear relationship between some force quantity $F$, mass $m$ and acceleration $\ddot{x}$. It is actually a very broad statement about potential energy minimization, momentum, trajectories, collisions, and can be used to directly derive equations in fluid dynamics, rigid body dynamics, and the general wave equation.

With great trepidation and humility I would like to suggest that the language of mathematics may be employed to reason about certain very well defined aspects of the gemara's logic in order to develop more sophistocated appreciation for the subtle, nuanced and perhaps misunderstood and seemingly convoluted thought process of the gemara.  

Consider the first two lines of the gemara on Sanhedrin 2b:

> ## מתני׳
>
> דיני ממונות בשלשה גזילות וחבלות בשלשה
>
> Monetary cases with three [judges]. Theft and injury with three. 
>
> (Sanhedrin 2a)

> ## :גמ׳
>
>  אטו גזילות וחבלות לאו דיני ממונות נינהו
>
> Gemara: But are thefts and injuries not [in the category] of monetary cases?
>
> (Sanhedrin 2b)

After staring at the first line of the mishna for a while and having some prior knowledge  about the laws of monetary, theft and injury cases leads to an immediate seeming contradiction; that the ruling for gzelot and chavelot are written independently as opposed to being omitted suggests they are distinct categories separet from mamonot. This is at odds with a prior rule that they are in fact included in the category of mamon. We shall now attempt to resolve the difficulty in the gemara by making a formal model of the gemara, analyze the model, and translate our results into something with halachic-logical semantic meaning.

It is important to bear in mind the idiosyncratic nature of the formal system we will be using. The objective is not to impose a logical structure on the gemara but to find a rigorous model with predictive and descriptive power that best fits the nature of the gemara itself.  Because of the exhibitionary nature of this document, I will not go into the details underlying my choice of logical system but comment that it emerges from observations in hindsight of how the gemara operates.

Firstly, we know we will be studying a logical system in which statements are either true or false. Secondly, we have some axiomatic notion that the gemara must be internally consistent. Contradictions between statements must either be resolved or one of the statements proven necessarily false; in other words any problem is the result of false assumptions.   

With this understanding, we may begin.

For some set of truths in the gemara, we denote the $n^{th}$ truth as a function of the state $s$ of assumptions and other truths in the system with the notation $P_{n}(s)$. Defining truths as a function of the variable state of the system  allows most inconsistencies in the system to be resolved by proving only one truth for each state of the halachic system. In formal terms, we can resolve seeming inconsistencies by proving injectivity for the statements in question. This formulation acknowledges that in gemara the truth itself is a computative process based on the current assumptions. It is possible and likely that for two different moments in the process of the gemar's *shakla vetarya* there is a logical inconsistency between two truths $P_{n}(s_1) \wedge P_{n}(s_0) = 1$, where $s_1 \ne s_0$but not for the same set of assumptions may there be two different truths. With this in mind, we can begin analyzing the first gemara in Sanhedrin:

Let $M$ be the set of words in the first sentence of the mishna, $n$ be the word *mamonot*, $g$ the word *gezelot*, $ch$ the word *chavelot*, and the category denoted by a word $q$  as $C(q)$; so the set of all gezelot cases is $C(g)$.

The gemara begins with an implied rule, let us call it $R(s_1)$[^1]

[^ 1]: This is not a definition of the rule function $R(t)$ in the sense that $f(x)= x + 2$ defines the mapping $f$ but a declaration of a specific instance of $R(s=s_1)$ in the sense that $f(x = 2)= 4$.

$$
R(s_1): n, g, ch \in M\implies \text{C}(g)  ,  \text{C}(ch) \not\subset C(n)\qquad
$$

Meaning, that because all three of gezelot, chavelot and mamonot are stated in the mishna instead of only mamonot, the categories of gezelot and chavelot must not be part of the category of mamonot.[^a] We know this from our initial analysis but are restating it formally.

[^a]: There are further assumptions here in terms of what a category is, that mamonot, gezelot and chavelot denote categories, etc. "It is left as an exercise to the reader…"

The mishna having $n, g, ch \in M$, results in the truth

$$
P(s_1): C(g), C(ch) \not\subset C(n) \qquad
$$

But $P(s_1)$ contradicts another prior truth for some state $s_0$

$$
P(s_0): C(g), C(ch) \subset C(n)
$$

This presents the possibility of a contradiction if $s_1=s_0$.

In order that the system not be inconsistent, **the gemara must prove that $P(s)$ is injective** for $s\in \{s_1, s_2\}$ (at least locally injective. once we define state and a way of enumerating over states we can prove global injectivity).

Now we have a well defined problem we can endeavor to find a set of states s.t. we may prove $P(s)$ to be injective. We can begin be considering how to permute the assumptions we currently have to arrive at one $s_0\ne s_1$ supporting $P(s_0)$.  Looking back at our initial assumptions, we see that

$$R(s_1) \implies P(s_1)$$

However, we may suggest an alternative state $S_0$ in which $R(s_1) \not \implies P(s_1)$. This would manifest itself in the implication

$$
R(s_0): n, g, ch \in M \not\implies C(g), C(ch) \not\subset C(n) \qquad
$$

or alternatively, we may define $R(s_0)$ as

$$
R(s_0): n, g, ch \in M \implies C(g), C(ch) \subset C(n) \qquad
$$

either way, we have an $s_0$ such that

$$
R(s_0)\implies P(s_0)
$$

which means there is some state $s_0$ in which $P(s_0)$ is true. If these two states are different and we can prove $R(s)$ is injective on $\{s_0, s_1\}$ then  $P(s)$ is also injective and therefore there is no inconsistency. Now we have a prediction of what might resolve the gemara's question of inconsistency, let us read ahead to see how the gemara answers:

> אמר רבי אבהו – Rabbi Abahu said
>
> מה הן קתני – [The Mishnah teaches an exhaustive list] to teach us what is [in the category of mamonot]
>
> מה הן דיני ממונות גזילות וחבלות  – [In order that we should know] What are monetary cases? [They are] Thefts and injuries.

In other words, Rav Abahu is suggesting the second of our two predictions for $R(s_0)$. This possibility was implicit in our formalization of the logic. Here we see that as soon as a local halachic situation can be fully formulated, the resolution to a claim of inconsistency may be found to be implied by the formulation itself.

The inquisitive reader may already have asked the great question: how to prove $R(s)$ is injective so that it is certain there is no inconsistency on $R$. We must prove $s_0\ne s_1$. However, we must be vigilant not to attempt to prove consistency of an arbitrary order distinction between the meta rules governing $R$. If so, we will will spiral into a trap of recursion or else circular logic unless we ultimately define some axioms governing $s$ which may be a function of any number of things; a function of location, a function of individual, etc[^b]

[^b]: Precisely when we try to define a function for state, does halacha refuse to be modellable and instead become become intuitive.[^2] Therefore we assume that the state function is at least continuous whatever that means [^3] so that halacha is locally modellable for the purposes of analyzing it.

Now if we stare at our conclusion for a while, we might remember the mishna obeys a rule of parsimony, i.e. there is some extra bit of information conveyed by all words in the mishna. 

The formal method of analysis is far from complete but this initial result is exciting. It shows that a formal system exists satisfying the constraints of accuracy and predictability at least on a local state interval ($\{s_0,s_1\}$). We can understand that in this formulation of logic, the break case for a halachic computation is satisfiably proving *psak*[^4] to be an injective function of state, which we have suggested is true. There is a far reaching and deep rooted logical structure to the gemara with very concrete goals and very real assumptions with poignant implications. It shows us the concept of *eilu ve'eilu* which is dependent on heuristic state.

**As a Software System**

I was conceptualizing a software system in which one may interact with the gemara as a network. Each individual chakira is represented as a node which may assume a binary state. Toggling the state of an upstream chakira to be one or the other opinion influences the ultimate output. In this software, one may toggle the assumptions of each chakira (eg: whether half damages fall under the set of penalties or of compensatory payments, or whether shaliach is fundamentally an extension of the body or fulfilling the word of his commander) and see how this changes the corollaries. However, because at its core the system performs computational logic, to a certain limited extent the system would be able to compute assumptions or find the set of node states including possibly discovering latent states necessary for a certain assertion to be true or false or prove that no such state exists. What is the total set of conditions in which X is liable for Y? I can imagine a very polished instance of this software being a powerful teaching tool. This will enable many people who may before have seen the gemara's logic to be convoluted to now percieve tremendous order and brilliance.

It is important to note I no not believe in the anachronistic notion that the chachomim actually using formal logic to derive halacha. I am offering an idea I had which helps me understand gemara and ultimately the halachic system which is the philosophical basis of the hashem's universe. May we be *zoche* to continue to advance in our torah learning and grow in our understanding and that this should lead to the most complete and meaningful service of our Creator.



[^2]: See *Meta-Halacha* for a brilliant explanation of this
[^3]: We have been vague about what the state actually is and what structures it is defined with.
[^4]: Here it wasn't immediately psak halacha, but the implications definitely are.
