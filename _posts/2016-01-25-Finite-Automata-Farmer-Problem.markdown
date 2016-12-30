---
title: Finite State Automata and the Farmer River Crossing Problem
layout: post
---

Recently from one of my mailing lists I was presented with the classic problem of solving for how a farmer with a goat, fox and cabbage best transport them all across a river without leaving any predator alone with its prey. You may have head this problem as one of its variants, but the main idas come through. .

The problem, formally defined:
> A farmer wants to cross a river and take with him a wolf, a goat, and a cabbage. There is a boat that can fit the farmer plus either the wolf, the goat, or the cabbage. If the wolf and the goat are alone on one shore, the wolf will eat the goat. If the goat and the cabbage are alone on the shore, the goat will eat the cabbage.
> **How can the farmer bring the wolf, the goat, and the cabbage across the river?**

I think this problem is interesting not from a problem solvers perspective, because solving it by hand is trivial,  but from the perspective of a programmer with a mathematical disposition.
It presents the opportunity to explore the idea of representing and solving a problem using math. This structured approach is very powerful for solving much larger problems of greater complexity.

Our problem can be solved with [deterministic finite state automata](https://en.wikipedia.org/wiki/Finite-state_machine), mathematical models of computation conceived as an abstract machine that can assume any number of states.

A finite state automaton is formally represented by a 5-tuple $(Q,\Sigma,\delta,q_0,F)$, where:

- $Q$ is a finite set of states the automaton can assume
- $\Sigma$ is a finite set of input symbols to the automaton
- $\delta$ is the transition function, translating a state and an input into a new state, $\delta(Q_k, \Sigma_i)=Q_j$
- $q_0$ is the starting state of the automaton, and the state before any input has been processed, where $q_0∈ Q$.
- $F$ is a set of states of $Q$,  $F\subset Q$ called accept states that terminate the running process of the automaton.

The farmer river crossing problem can be represented as a finite state automaton. We make $Q$ is the set of all states, i.e, the set of all vectorized representations of which object is on which side of the river. We make $\Sigma$ the set of all possible river crossings and $δ(Q_k, \Sigma_i)$, the transition function, apply the movement $\Sigma_i$ to the state $Q_k$ and return a new state.

To solve the problem, we will find the set of transitions $\Sigma'$ such that applying them in sequence to $Q_0$ yields $F$, our accept state.

We can define the set of all states $Q$ by finding every permutation of a four length vector, where the value at each index can assume two states.

We define our permute function. The details of how it works are unnecessary, but if you are interested, it uses a modified form of breadth first search which traces all paths to the root nodes and returns them.


```python
def permute(s,n):
    seq=range(s)
    permutations = []
    nodes = list(seq)
    while len(permutations) < s**n:
        node = nodes.pop(0)
        children = list(seq)
        permutation = permutations.pop(0) if len(permutations)>1 else []
        for i in range(len(children)):
            perm = list(permutation)
            perm.append(children[i])
            permutations.append(perm)
            nodes.append(children[i])
    return permutations
```

And generate the set of all states, $Q$, as a 4-lengthed vector, where $Q_i$ represents the side of the river on which the $i^{th}$ object currently sits, $0$ being the starting side and $1$ the other side, ordered sequentially as Farmer, Fox, Goat, Cabbage.


```python
Q = permute(2,4)
```

The names map to indices in Q. So if `names = ["Man", "Fox", "Goat", "Cabbage"]`, then Q[0] tells us which island the man is on.

We also create a cute little helper function $Q_x$ giving the numerical representation of the state-vector q. This will be useful in the future


```python
Qx = lambda q: Q.index(q)
```

With Q, we can define $F$ as the last state in $Q$:


```python
F = Q[-1]
```

Now we generate $Σ$ the set of all possible state transitions – the set of all movements across the river – as a 3-tuple $e$ where $e_0$ is the side $0$ or $1$ to which the farmer, $e_1$ and another object $e_2$ are travelling.


```python
E = [ (i, 0, j) for i in [1,0] for j in range(4)]
```

Our transition function $T$, returning the new state given the current state and an input.


```python
T = lambda q, i: [ i[0] if i[1] == j or i[2] == j else q[j] for j in range(len(q))]
```

We define some helper functions.

$valid(q_i)$ tells us whether a given state is valid and $transition(q_i)$ returns the set of all states $q_i$ can transition to. $valid\_transitions(q_i)$ returns all valid states $q_i$ can transition to.


```python
prohibited = [(1,2),(2,3)]
valid = lambda q: not (sum([q[p[0]]==q[p[1]] and q[0]!=q[p[0]] for p in prohibited]) > 0)
transition = lambda q: [ (e, Qx( T(q,e) )) for e in E if e[0]!=q[0] and e[0]!=q[e[2]]]
valid_transitions = lambda q: [ n for n in transition(q) if valid(Q[n[1]])  ]
```

Now we can make a graph depicting all states and their relationships to eachother. The starting state is depicted in yellow, all invalid states are depicted in red, and the ending state $F$ in green.


```python
import matplotlib.pyplot as plt
%matplotlib inline
import networkx as nx
G = nx.DiGraph()
for q in Q:
    G.add_node(Qx(q))

for q in Q:
    children = transition(q)
    for c in children:
        G.add_edge( Qx(q), c[1],transition=c[0])

labels = {}

for q in range(len(Q)): labels[q] = "${0}$".format(Q[q])

plt.figure(2,figsize=(15,10))
pos = nx.graphviz_layout(G)


def color(q):
    if q==F: return "#2ECC71"
    if q == Q[0]:   return "#F39C12"
    return "#446CB3" if valid(q) else "#F22613"

nx.draw_networkx(G,
                 pos,
                 with_labels=True,
                 labels={q: "${0}$".format(Q[q]) for q in range(len(Q))},
                 node_size=2000,
                 node_color=[color(q) for q in Q])


```


![png]({{site.url}}/images/Finite-Automata_files/Finite-Automata_16_0.png)


We could find the solution graphically, but I say we solve the problem using code.

We use **breadth first search** to find and trace the shortest between the starting state and our accept state $F$. Solve returns the set of transitions that brings us from $q_0$ to $F$


```python
def solve(q):
    not_visited = range(len(Q))
    paths = []
    nodes = [Qx(q)]
    while not_visited:
        node = nodes.pop(0)
        children = valid_transitions(Q[node])
        path = paths.pop(0) if len(paths)>0 else []
        for i in range(len(children)):
            child = children[i][1]
            if child in not_visited:
                not_visited.remove(child)
                newpath = list(path)
                e = children[i][0]
                newpath.append(e)
                paths.append(newpath)
                nodes.append(child)
                if (child == Qx(F)):
                    return newpath
    return paths
```

And we solve for the solution


```python
solution = solve(Q[0])
solution
```




    [(1, 0, 2), (0, 0, 0), (1, 0, 1), (0, 0, 2), (1, 0, 3), (0, 0, 0), (1, 0, 2)]



We can verify this solution works visually by getting the node traversal history for our transition history and cross checking it with our graph above. Indeed, both node histories match, so we have our solution.


```python
q = Q[0]
print q
for e in solution:
    q = T(q,e)
    print q

```

    [0, 0, 0, 0]
    [1, 0, 1, 0]
    [0, 0, 1, 0]
    [1, 1, 1, 0]
    [0, 1, 0, 0]
    [1, 1, 0, 1]
    [0, 1, 0, 1]
    [1, 1, 1, 1]


Now let's print that solution out in a human readable way.


```python
names = ["Man", "Fox", "Goat", "Cabbage"]

for transition in solution:
    print "Move the {0} and {1} to Island {2}".format(
        names[transition[1]],
        names[transition[2]],
        transition[0])

```

    Move the Man and Goat to Island 1
    Move the Man and Man to Island 0
    Move the Man and Fox to Island 1
    Move the Man and Goat to Island 0
    Move the Man and Cabbage to Island 1
    Move the Man and Man to Island 0
    Move the Man and Goat to Island 1


Looks like this works. Harnessing graph theory and finite state automata, we've enabled the farmer and his entourage to successfully and safely get home.

## SOLVED!

**EDIT:** I wrote a [reflection on this post](https://medium.com/@theideasmith/harnessing-graph-and-automata-theory-to-solve-the-farmer-river-problem-8c4a94743a9e#.90zf1gajt) for my medium blog.



```python

```
