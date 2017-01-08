---
otherlangs: he
layout: post
author: Akiva Lipshitz
title: A Tool for Developing an Understanding of Nuance and Subtlety in Gemara
date: 12-9-16

---

# Formal Logic as a Tool for Analyzing Gemara

## Akiva Lipshitz

### Developed over the course of December 9, 2016 to January 6, 2017

An open mindedness to novel approaches to Gemara learning transforms the formal system of mathematical reasoning into a tool to aid the student – or possibly the expert – in their endeavors to  dissect Gemara and develop a greater appreciation for its nuanced and hidden logical structure. Formal languages offer two innovations: (1) their well defindedness allows for objective exploration of the solution space to an issue. One need only to consider the necessary formal conditions of a solution and contemplate which formal truths lead the system in that direction. (2) expressions in formal languages make much broader implicit statements. Therefore, making a formal statement about an otherwise subjective issue represents a major step in the direction of a solution to the issue.  

With great trepidation and humility I would like to suggest that the language of mathematics may be employed to reason about certain very well defined aspects of the gemara's logic in order to develop more sophistocated appreciation for the subtle, nuanced and perhaps misunderstood and seemingly convoluted thought process of the gemara.  

I propose a logical model for stating Talmudical assertions. By inspecting a logical model we can  hypothesis solutions. Of course, a formal solution is only relevant if it has a corresponding semantic meaning.  

Before proceeding to describe the model used here, it is important to bear in mind its idiosyncratic nature. My objective is not to impose a logical structure on the gemara but to find a rigorous model with predictive and descriptive power that best fits the nature of the Gemara's logic itself.  The particular implications and assumptions of the system I use are arbitrary and were made as intuitive guesses as to what kind of a system is best for analyzing the logical flow of the Gemara. 

Some guiding notions to the model are (1) we know we will Talmudic logic is binary; statements are either true or false. (2) there is an obvious axiomatic notion that the Gemara must be internally consistent. Contradictions between statements must either be resolved or one of the statements proven necessarily false; in other words any problem is the result of false assumptions. (3) Talmudical logic can span multiple orders of scope, as per its usage in computer science. The scope of the narrator manages and is aware of the global logic, and comments of sages mentioned therein are usually independent entities of scope relative to the global scope. Our system shall operate at the same level of scope as that of the narrator and not above it. This means the system itself cannot operate on narrative comments as first class objects; the computations that resolve the Gemara must be performed by a human observer and cannot be specified within the system itself. [^1]

[^1]: This limitation is similar to most formal mathematics in which the proof creation process cannot be specified at the same level of scope as the mathematical theory itself. The exception to this might be the lambda calculus, although seeing to my having not studied it, this is only a postulation.

With this understanding, consider the following formulation of a system for encapsulating Talmudic logical flows and analyzing them:

### Example I

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

After staring at the first line of the mishna for a while and having some prior knowledge  about the laws of monetary, theft, and injury case, an immediate seeming inconsistency arises; the fact that the ruling for gzelot and chavelot are written in addition to that of monetary cases signals they are a distinct entity. However, prior information asserts that is not the case. 

We shall now attempt to resolve this difficulty by establishing the Gemara in formal terms and proceeding to analyze the formal model. 

The Gemara some set of truths in the gemara, we denote the $n^{th}$ truth as a function of the state $s$ of assumptions and other truths in the system with the notation $P_{n}(s)$. Defining truths as a function of the variable state of the system  allows most inconsistencies in the system to be resolved by proving only one truth for each state of the halachic system. In formal terms, we can resolve seeming inconsistencies by proving injectivity for the statements in question. This formulation acknowledges that in gemara the truth itself is a computative process based on the current assumptions. It is possible and likely that for two different moments in the process of the gemar's *shakla vetarya* there is a logical inconsistency between two truths $P_{n}(s_1) \wedge P_{n}(s_0) = 1$, where $s_1 \ne s_0$but not for the same set of assumptions may there be two different truths. With this in mind, we can begin analyzing the first gemara in Sanhedrin:

Let $M$ be the set of words in the first sentence of the mishna, $n$ be the word *mamonot*, $g$ the word *gezelot*, $ch$ the word *chavelot*, and the category denoted by a word $q$  as $C(q)$; so the set of all gezelot cases is $C(g)$. 

The gemara begins with an implied rule, let us call it $R(s_1)$[^2] 

[^ 2]: This is not a definition of the rule function $R(t)$ in the sense that $f(x)= x + 2$ defines the mapping $f$ but a declaration of a specific instance of $R(s=s_1)$ in the sense that $f(x = 2)= 4$.

$$
R(s_1): n, g, ch \in M\implies \text{C}(g)  ,  \text{C}(ch) \not\subset C(n)\qquad
$$

Meaning, that because all three of gezelot, chavelot and mamonot are stated in the mishna instead of only mamonot, the categories of gezelot and chavelot must not be part of the category of mamonot.[^3] We know this from our initial analysis but are restating it formally. 

[^3]: There are further assumptions here in terms of what a category is, that mamonot, gezelot and chavelot denote categories, etc. "It is left as an exercise to the reader…"

The mishna having $ n, g, ch \in M$, results in the truth 
$$
P(s_1): C(g), C(ch) \not\subset C(n) \qquad
$$
But $P(s_1)$ contradicts another prior truth for some state $s_0$
$$
P(s_0): C(g), C(ch) \subset C(n)
$$
This presents the possibility of a contradiction if $s_1=s_0$.

In order that the system not be inconsistent, **the gemara must prove that $P(s)$ is injective** for $s\in \{s_1, s_2\}$ (at least locally injective. once we define state and a way of enumerating over states we can prove global injectivity). 

Now we have a well defined problem we can endeavor to find a set of states s.t. we may prove $P(s)$ to be injective. We can begin be considering how to permute the assumptions we currently have to arrive at one $s_0\ne s_1$ supporting $P(s_0)$.  Looking back at our initial assumptions, we see that $R(s_1) \implies P(s_1)$. However, we may suggest an alternative state $S_0$ in which $R(s_) \not \implies P(s_1)$. This would manifest itself in the implication
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

The inquisitive reader may already have asked the great question: how to prove $R(s)$ is injective so that it is certain there is no inconsistency on $R$. We must prove $s_0\ne s_1$. However, we must be vigilant not to attempt to prove consistency of an arbitrary order distinction between the meta rules governing $R$. If so, we will will spiral into a trap of recursion or else circular logic unless we ultimately define some axioms governing $s$ which may be a function of any number of things; a function of location, a function of individual, etc.

Now, realize that precisely when we try to define a function for state, does halacha refuse to be modellable and instead necessarily become a product of human intuition. [^5] Therefore we assume that the state function is at least continuous whatever that means [^6] so that halacha is locally modellable for the purposes of analyzing it.

The formal method of analysis is far from complete but this initial result is exciting. It shows that we can formully depict a Talmudic logical flow satisfying the constraints for it to both accurately represent the actual Talmudic flow and have inherent predictive power at least on a local state interval $\{s_0,s_1\}$.

### Example II

**As a Software System**

I was conceptualizing a software system in which one may interact with Talmudic flow as a network of logical assertions. Each individual chakira can be represented as a node which assumes a binary state. Toggling the state of an upstream chakira to be one or the other opinion propagates changes through to downstream nodes. For example, toggling global state $s_g$ between $s_0$ and $s_1$ in **example I** would result in changes to the value of $P(s_g)$. One may toggle, for example, the assumption of whether half damages fall under the set of penalties or of compensatory payments, or whether shaliach is fundamentally an extension of the body or fulfilling the word of his commander, and see how this changes the corollaries. 

At its core the system would be built atop a computational logic system, and therefore to a certain limited extent would be able to compute answers to questions. It could compute assumptions of an assertion or find the set of node states, including possibly discovering latent states, necessary for a certain assertion to be true or false or prove that no such state exists. What is the total set of conditions in which $X$ is liable for $Y$? I can imagine a very polished instance of this software actually igniting people's latent appreciation for the tremendous order and brilliance of the Gemara's thought process.

We can understand that in this formulation of logic, the break case for a halachic computation is satisfiably proving *psak*[^7] to be an injective function of state, which we have suggested is true. There is a far reaching and deep rooted logical structure to the gemara with very concrete goals and very real assumptions with poignant implications. It shows us the concept of *eilu ve'eilu* which is dependent on heuristic state. 

It is important to note I no not believe in the anachronistic notion that the chachomim actually using formal logic to derive halacha. I am offering an idea I had which helps me understand gemara and ultimately the halachic system which is the philosophical basis of the hashem's universe. May we be *zoche* to continue to advance in our torah learning and grow in our understanding and that this should lead to the most complete and meaningful service of the Creator. 

[^5]: See *Meta-Halacha* (pg. 34, "Halacha and Nonmodelability") for a brilliant explanation of this.
[^6]: We have been vague about what the state actually is and what structures it is defined with.
[^7]: Here it wasn't immediately psak halacha, but the implications definitely are.
