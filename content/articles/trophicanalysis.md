Title: Trophic Coherence
Date: 2021/02/08
Tags: econ, math
Authors: Andrea Titton
Summary: A primer on trophic coherence


#### This post uses the notation of the awesome paper by [MacKay, Johnson, and Sansom](https://arxiv.org/abs/2001.05173) (2020). Definitely check it out!

### What is it?


<img src="https://github.com/NoFishLikeIan/trophic-resilience/blob/master/plots/presentations/electricity.png?raw=true" height="250px" style="float: left"/> 

Imagine you face the weighted directed graph on the side and you know there is some interdependency of sort. You want to figure out which node, if removed, could hinder the stability of the dynamical process you have in mind.

The most intuitive thing you can do is to look at the graph Laplacian operator $$\Lambda = \text{diag}(u) - W - W^T,$$ where $W$ is the weight matrix and $u$ is the total weight vector (i.e. the sum of in- and out-weights for each node). I like to think of it (improperly) as the graph analog of the Laplace operator $\nabla^2$ which is a key operator to study a diffusion process on functions. So it makes sense that when you think of diffusion processes on a network structure you look at $\Lambda$.

Here is where the trophic level comes in: it is the vector $h$ that solves,

$$
\Lambda h = v, \text{ where }v = w_{in} - w_{out}.
$$

### ...so what?

This seems very much out of the blue. And it looked like it to me as well. Until I tried some examples myself!

Let's look at a very simple network. Imagine a system where we have plants 🌿, cows 🐮 that eat plants, and tigers 🐯 that eat both cows and plants, but the former to a lesser degree. This might look on the graph somewhat like this,

$$
W = \begin{pmatrix}
    0 & 0.95 & 0.2 \\
    0 & 0 & 0.5 \\
    0 & 0 & 0
\end{pmatrix}, \ 
x = \begin{pmatrix}
    🌿 \\ 🐮 \\ 🐯
\end{pmatrix}.
$$

Then we can compute the weight and imbalance vector, 

$$
    u = \begin{pmatrix}
        0 \\ 0.95 \\ 0.7
    \end{pmatrix} + \begin{pmatrix}
        1.15 \\ 0.5 \\ 0
    \end{pmatrix} = \begin{pmatrix}
        1.15 \\ 1.45 \\ 0.7
    \end{pmatrix} \text{ and }
    v  = \begin{pmatrix}
        -1.15 \\ 0.45 \\ 0.7
    \end{pmatrix}.
$$

Then the trophic level of each animal $h$ solves $\Lambda h = v$ or in numbers 

$$
\begin{pmatrix}
    1.15 & -0.95 & -0.2 \\
    -0.95 & 1.45 & -0.5 \\
    -0.2 & -0.5 & 0.7
\end{pmatrix} \cdot \begin{pmatrix}
    h_{🌿} \\ h_{🐮} \\ h_{🐯}
\end{pmatrix} =  \begin{pmatrix}
        -1 \\ 0 \\ 1
    \end{pmatrix} \implies \begin{pmatrix}
    h_{🌿} \\ h_{🐮} \\ h_{🐯}
\end{pmatrix} \approx \begin{pmatrix}
    -0.97 \\ -0.10 \\ 0.64
\end{pmatrix}.
$$

This is a very interesting result. It tells us at what "level" of the food chain each node is!

This gives as a nice metric of how "coherent" the network is! We can just look at the (weighted scaled) variance of this value, 

$$
F_0 = \frac{\sum w_{i, j} \cdot (h_{i} - h_j - 1)^2}{\sum w_{i, j}}
$$

### ...what does this tell us?

Ok. We have a food chain estimate. Now imagine a [Lotka-Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) type of dynamic for the population. If we start with a vector $x$ with the population of 🌿, 🐮, 🐯. The dynamics is then,

$$
\dot{x}_🐮 = x_🐮 \cdot \left(\underbrace{R_🐮}_{\textit{born}} + \underbrace{W_{🌿, 🐮} \cdot x_🐮}_{\text{eat}} - \underbrace{W_{🐮, 🐯} \cdot x_🐮}_{\text{be eaten}} \right).
$$

The stability of the dynamics depend on $F_0$! 

I have the proof but it does not fit in the narrow margin here.

### ...why do care?

I can give you some empirical reasons.

- Does not require basal/terminal nodes,
- Robust to cycles,
- Is between $[0, 1]$,
- Comparable among different graphs,
- Results hold on partial graphs.

There are also some inherently theoretical reasons and in particular in economics, where the networks are often cyclical and very complex, this metric can serve us very well. 

So go back to your model writing and try and derive it!


<br> </br>
<br> </br>