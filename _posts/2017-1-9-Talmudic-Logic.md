---
otherlangs: he
layout: post
author: Akiva Lipshitz
title: Formal Logic as a Tool for Analyzing Gemara
date:   2017-1-6
---

The formal system of mathematics can be used as an innovative tool in the study of Gemara. It offers great value as a technique for the student to use in their endeavors to dissect and develop a greater appreciation for the Gemara's highly complex and nuanced logical structure. 

Formal languages offer two possible innovations to Gemara study: (1) their well defindedness makes it easier to theorize about possible situations. Because statements in formal languages are easily permuted or manipulated, the space of possible solutions or reformulations of a formally stated problem can be easily explored. (2) decivingly simple expressions in formal languages can actually be making much broader implicit statements too, which are much easier to discover when the statements themselves are so well defined. Making a formalization of a seemingly intractable issue in Gemara can represent a major step in the direction of a solution. 

Understanding the bold nature of this idea, with great trepidation and humility I would like to suggest that the language of mathematics may be employed to reason about certain very well defined aspects of the gemara's logic. If used correctly, it can actually help yield a more sophistocated appreciation for the subtle, nuanced and perhaps misunderstood and seemingly convoluted thought process of the gemara.  

This short essay will only discuss my initial thoughts on this matter, which I hope to develop in due time into a broader methodology. Perhaps I will discover the methodology is better suited to be used intuitively as opposed to rigorously and formally, and if so, that will be the case. Here, I propose a logical model for stating and analyzing assertions in the Gemara. By inspecting a logical model we can  hypothesis solutions. Of course, a formal solution is only relevant if it has a corresponding semantic meaning.  

Before proceeding to describe the model used here, it is important to bear in mind its idiosyncratic nature. My objective is not to impose a logical structure on the gemara but to find a rigorous model with predictive and descriptive power that best fits the nature of the Gemara's logic itself.  The particular implications and assumptions of the system I use are arbitrary and were made as intuitive guesses as to what kind of a system is best for analyzing the logical flow of the Gemara. 

Some guiding notions to the model are

1. That for the most part states in halacha are binary; no states are subjectively defined in the Gemara. Even though the notion of *safek* seems to be probabalistic, it is in fact used as if it were a binary variable.  
2. There is an obvious axiomatic notion that the Gemara must be internally consistent. Contradictions between statements must either be resolved or one of the statements proven necessarily false; in other words any problem is the result of false assumptions. 
3. Talmudical logic can span multiple orders of scope, as per its usage in computer science. The scope of the narrator manages and is aware of the global logic, and comments of sages mentioned therein are usually independent entities of scope relative to the global scope. Our system shall operate at the same level of scope as that of the narrator and not above it. This means the system itself cannot operate on narrative comments as first class objects; the computations that resolve the Gemara must be performed by a human observer and cannot be specified within the system itself. [^1]

[^1]: This limitation is similar to most formal mathematics in which the proof creation process cannot be specified at the same level of scope as the mathematical theory itself. The exception to this might be the lambda calculus, although seeing to my having not studied it, this is only a postulation.

Anyone who has learned Gemara b'iyun will understand that much of the halachic discourse, *shakla vetarya*, is precipitated on the Amoraim, Rishonim, etc. having differing perspectives which leads to their own distinct approaches to any issue. What the ultimate psak is depends on which of these approaches the halachic powers that be accept upon themselves. In the era of the Beit Hamikdash, the *Anshei Kineset Hagedolah* (AKH) would debate amongst themselves and eventually a psak would be reached and accepted as binding; anyone who disagreed with the ruling of the AKH would be a *zaken mamrei*. Continuing into modern times, the ultimate psak depends on which approach is accepted; different communities follow different approaches. 

We will build our formal model keeping in mind that psak depends on the halachic perspective of the posek. This will be represented by what we shall call halachic state, and denote by convention with the letter $s$. For example, in the famous debate about the nature of a shaliach, there are at least two possible approaches: (1) either the shaliach is an extension of the ba'al's own hand, or he is an entirely separate entity. Which of these two approaches is held by the halachic powers that be determines any subsequent rulings that depend on the definition of a shaliach. 

Our model can define psak as a function of state. Say you want to know the consequences of a shaliach failing to perform a mitzvah properly. You can think of the answer to this question being a function of the accepted definition of shaliach. 

In general, we can define a psak function denoted by the symbol $h(s)$, where $h$ is a placeholder that here stands for *halacha*, and metaphorically consult this function when we want to know the psak on a certain issue. In our shaliach case, where we want to examine the consequences for a shaliach failing to properly execute the mitzvah he is sent to perform, we might consult a function of the form 
$$
\text{liability-of-shaliach}(\text{definition of shaliach})
$$
This is just hypothesizing, but if the shaliach is an autonomous entity, separate from the ba'al, then perhaps he would be liable. However, if he is an extension of the ba'al's hand then the ba'al might be liable. I'll have to do my research on this question. 

Defining the halachic psak as a function of state, or the assumption, derives immediately from the nature of the Gemara itself. As anyone who has studied Gemara will know, much of the disagreement is founded upon there existing fundamentally different approaches to an issue. Taking this into account is absolutely essential for the design of our formal model to represent the Gemara's flow of logic. Otherwise, if instead of defining psak as a function of state we merely defined it statically, then the model would be unable to account for differences of opinion. 

Much of Gemara revolves around resolving what seems to be a contradiction. In our model, this would amount to having a function of psak for a particular case, let us call it $p(s)$. A seeming contradiction arises if we have $p(s_1) = \neg p(s_2)$. To resolve this, we must either prove that $p$ is indeed a function, that is for each $s$ there is exactly one $p(s)$, or that $s_1\not = s_2$. 

It is possible and likely that for two different moments in the process of the gemara's *shakla vetarya* there is a logical inconsistency between two truths $P_{n}(s_1) \wedge P_{n}(s_0) = 1$, where $ s_1 \ne s_0$ but for the same set of assumptions there may never be two contradicting truths. 

We shall now demonstrate a simple usage of this approach by analyzing the first Gemara in Sanhedrin. 

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

---

Let $M​$ be the set of words in the first sentence of the mishna, and $C_\text{word}​$ be the category denoted by the word $word​$; so the set of all gezelot cases is $C_\text{gezelot}​$. 

The gemara begins with an implied rule, let us call it $R(s_1)$[^2] 

[^2]: This is not a definition of the rule $R(t)$ in the sense that $f(x)= x + 2$ defines the mapping $f$ but a declaration of a specific instance of $R(s=s_1)$ in the sense that $f(x = 2)= 4$.


$$
R(s_1): \text{mamonot, gezelot, chavelot} \in M\implies C_\text{gezelot}  ,  C_\text{chavelot} \not\subset C_\text{mamonot} \qquad
$$



Meaning, that because all three of *gezelot*, *chavelot* and *mamonot* are stated in the mishna as dinstinct words, the categories of gezelot and chavelot must not be part of the category of mamonot.[^3] We only *mamonot* stated, we would assume *gezelot*, and *chavelot* to be part of mamonot.  We already know this from our initial analysis but are restating it formally for the sake of demonstration. 

[^3]: There are further assumptions here in terms of what a category is, that mamonot, gezelot and chavelot denote categories, etc. "It is left as an exercise to the reader…"

The mishna having $ \text{mamonot, gezelot, chavelot} \in M$, allows us to apply $R(s_1)$ and have $P(s_1)$



$$
P(s_1): C_\text{gezelot}  ,  C_\text{chavelot} \not\subset C_\text{mamonot}
$$



But, as we saw in our initial analysis of the mishna, there is another truth, $P(s_0)$, for some other state $s_0$ that contradicts$P(s_1)$:



$$
P(s_0): C_\text{gezelot}  ,  C_\text{chavelot} \subset C_\text{mamonot}
$$



Now, if $s_0 = s_1$, then we have a contradiction between $P(s_1)$ and $P(s_0)$, and therefore a halachic inconsistency!

In order to show this is not so, **the gemara must prove that $P(s)$ is a function** over $s\in \{s_1, s_2\}$, or that $s_1 \not = s_2$. 

## Making the Move

Now that we have a well defined problem we can endeavor to find a set of states s.t. we may prove $P(s)$ to be a function as opposed to just a relation. We can begin our approach by considering how to permute our current assumptions with the hopes that we will arrive at a point where it is likely that $s_0\ne s_1$ , which would show no inconsistency. Looking back at our initial assumptions, we see that $R(s_1) \implies P(s_1)$. This means that if we can find some other rule $s_0$ for  which $R(s_0) \not \implies P(s_1)$, but $R(s_0) \implies P(s_0)$ then we will have negated the inconsistency by showing that $P(s_1)$ and $P(s_0)$ actually emerge from two different states. Well that is not difficult: all we must do is propose another rule $R(s_0)$ as the converse of $R(s_1)$:



$$
R(s_0):  \neg R(s_1) : \text{mamonot, gezelot, chavelot} \in M \not\implies C_\text{gezelot}  ,  C_\text{chavelot} \not\subset C_\text{mamonot} \qquad
$$



or, stating $R(s_0)$ in the positive as opposed to the double negative: 



$$
R(s_0): \text{mamonot, gezelot, chavelot} \in M \implies C_\text{gezelot}  ,  C_\text{chavelot} \subset C_\text{mamonot} \qquad
$$



either way, we have an $s_0$ such that

$$
R(s_0)\implies P(s_0)
$$


which means that  is some state $s_0$ in which $P(s_0)$ is true. Now, $R$ is the line of distinction between $P(s_0)$ and $P(s_1)$. If we can be certain that for any $s$ there is exactly one $R(s)$ then that means there is absolutely no inconsistency; each disjoint state has exactly one truth associated with it. 

> אמר רבי אבהו – Rabbi Abahu said
>
> מה הן קתני – [The Mishnah teaches an exhaustive list] to teach us what is [in the category of mamonot]
>
> מה הן דיני ממונות גזילות וחבלות  – [In order that we should know] What are monetary cases? [They are] Thefts and injuries. 

In other words, Rav Abahu is suggesting the second of our two predictions for $R(s_0)$. This possibility was implicit in our formalization of the logic. Here we see that as soon as a local halachic situation can be fully formulated, the resolution to a claim of inconsistency may be found to be implied by the formulation itself. 

That in our model effectively $s \implies R \implies P$ helps us understand the structure of the Gemar's logic here. Realize that precisely when we try to define a function for state, does halacha refuse to be modellable and instead necessarily become a product of human intuition. [^5] Why? Consider this. Either the state is $s_1$ in which case the initial rule $R(s_1)$ holds, or the state is $s_0$ and Rav Abahu's suggestion $R(s_0)$ holds. Thus, the ultimate ruling $P(S)$ is highly dependent on state is, in other words, which axioms are assumed. 



Therefore we assume that the state function is at least continuous whatever that means [^6] so that halacha is locally modellable for the purposes of analyzing it.

The formal method of analysis is far from complete but this initial result is exciting. It shows that we can formully depict a Talmudic logical flow satisfying the constraints for it to both accurately represent the actual Talmudic flow and have inherent predictive power at least on a local state interval $\{s_0,s_1\}$.

### Example II

**As a Software System**

I was conceptualizing a software system in which one may interact with Talmudic flow as a network of logical assertions. Each individual chakira can be represented as a node which assumes a binary state. Toggling the state of an upstream chakira to be one or the other opinion propagates changes through to downstream nodes. For example, toggling global state $s_g$ between $s_0$ and $s_1$ in **example I** would result in changes to the value of $P(s_g)$. One may toggle, for example, the assumption of whether half damages fall under the set of penalties or of compensatory payments, or whether shaliach is fundamentally an extension of the body or fulfilling the word of his commander, and see how this changes the corollaries. 

At its core the system would be built atop a computational logic system, and therefore to a certain limited extent would be able to compute answers to questions. It could compute assumptions of an assertion or find the set of node states, including possibly discovering latent states, necessary for a certain assertion to be true or false or prove that no such state exists. What is the total set of conditions in which $X$ is liable for $Y$? I can imagine a very polished instance of this software actually igniting people's latent appreciation for the tremendous order and brilliance of the Gemara's thought process.

I take these ideas futher in [this other paper currently being worked on](https://www.dropbox.com/s/8ze669u62wocquh/Gemara%20Logic.pdf?dl=0). 

---



We can understand that in this formulation of logic, the break case for a halachic computation is satisfiably proving *psak*[^7] to be at most a one-to-one function of the current state of assumptions and rules in the halachic system. There is a far reaching and deep rooted logical structure to the gemara with very concrete goals and very real assumptions with poignant implications. It shows us the concept of *eilu ve'eilu* which is dependent on heuristic state. 

It is important to note I no not believe in the anachronistic notion that the chachomim actually using formal logic to derive halacha. I am offering an idea I had which helps me understand gemara and ultimately the halachic system which is the philosophical basis of the hashem's universe. May we be *zoche* to continue to advance in our torah learning and grow in our understanding and that this should lead to the most complete and meaningful service of the Creator. 

[^5]: See *Meta-Halacha* (pg. 34, "Halacha and Nonmodelability") for a brilliant explanation of this.
[^6]: We have been vague about what the state actually is and what structures it is defined with.
[^7]: Here it wasn't immediately psak halacha, but the implications definitely are.
