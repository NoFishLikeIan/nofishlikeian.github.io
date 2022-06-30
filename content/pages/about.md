Title: About me 🦉
Date: 2021-02-03
Authors: Andrea Titton


<br/><br/>

<img src="{static}/images/palude.jpg" alt="drawing" width="600"/>


Hello! I am Andrea Titton, PhD candidate in Quantitative Economics at the [CENDEF group](https://cendef.uva.nl/), University of Amsterdam.

### PhD and Job Market Paper

<figure style="float: right; margin-left: 100px">
    <img src="{static}/images/basin_small.png" alt="drawing" width="450"/>
    <figcaption style = "text-align: center">A dynamical system over supply chain depth instead of time. </figcaption>
</figure>

I work on theoretical economics. Particularly **games on networks** and **endogenous production networks**. I am developing a model of suppliers' risk diversification to study the effect of firm decision on production network fragilities. I use techniques from dynamical systems and percolation theory and combine them with network games. The model shows that correlation among suppliers can reduce firm diversification. This introduces fragility in a production network even if risk is kept constant (The plot on 👉 shows the tipping point arising from this mechanism.)

Furthermore, I calibrate the model using graphon estimation techniques ([à la Pensky](https://arxiv.org/pdf/1607.00673.pdf)) on [CBS firm level data](https://www.cbs.nl/en-gb/onze-diensten/customised-services-microdata/microdata-conducting-your-own-research). I am trying to construct an index of correlation risk and relating it to other common techniques to determine network stability (e.g. [trophic analysis]({filename}/articles/trophicanalysis.md)).


### Cooperative game theory

I developed and mantain a Julia package to solve cooperative games ([CooperativeGames.jl](https://github.com/NoFishLikeIan/CooperativeGames.jl)). Defining a game is as simple as


```julia
players = collect(1:6)
links = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (5, 6)]
value(S::Players) = (1 ∈ S && 6 ∈ S) ? 1 : 0

G = GraphGame(players, value, links)
```

which gives you a lot of convenient and fast computational methods

```julia
isconvex(G)
fₛ(G) # Shapley value
graphtoMyerson(G) # Myerson formulation
degreeHarsanyi(G) # Harsanyi degrees
```

### NLP analysis and sustainability 

This is a joint work with the [Amsterdam Center for Law and Economics](https://acle.uva.nl/), partly funded by the [*A Sustainable Future*](https://asf.uva.nl/) grant.

Institutional investors have large voting power in many polluting firms. However, their engagement with portfolio companies is imperfectly observable. We infer it based on an NLP algorithm applied to investors' disclosures. We calculate the index for investors and study its relationship with CO2 emissions and ESG performance of portfolio companies.

### Motion Perception and Particle Filters

<figure style="float: right; margin-left: 100px">
    <img src="{static}/images/extrapolation.gif" alt="drawing" width="450"/>
    <figcaption style = "text-align: center">A particle filter model of motion extrapolation. </figcaption>
</figure>

We study the mechanism that allows the brain to compensate for neural delays. After collecting behavioural data on the illusion illustrated on the 👉, we calibrate a particle filter model, and show that it is consistent with the observed extrapolation.

### On the side
I love math and computers. I like playing around with [Prolog](https://github.com/NoFishLikeIan/prolog-playground) and [Clojure](https://github.com/NoFishLikeIan/dietary-monitor). I also do some recreational math. I love games of no chance, mainly chess and [domineering](https://webdocs.cs.ualberta.ca/~games/domineering/). Finally I am fascinated by [hot water bottles](https://solar.lowtechmagazine.com/2022/01/the-revenge-of-the-hot-water-bottle.html) and economic history.

### Reading now:

- [The Turn](https://www.theatlantic.com/past/docs/unbound/langew/turn.htm) by *William Langewiesche*
- The Story of Work by *Jan Lucassen*
- On Numbers and Games by *John Conway*

<br/><br/>

## Follow me...

- ...on
[<img src="https://raw.githubusercontent.com/carlsednaoui/gitsocial/master/assets/icons%20with%20padding/twitter.png">](https://twitter.com/accuian) for some random math and econ stuff with a spray of ranting in italian. 

- ...on [<img src="https://raw.githubusercontent.com/carlsednaoui/gitsocial/master/assets/icons%20with%20padding/github.png">](https://github.com/NoFishLikeIan) for some Julia, Python, Clojure, and occasional Prolog.

<br/><br/>
