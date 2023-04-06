Title: Code 🐙
Date: 2023-04-06
Authors: Andrea Titton

## CooperativeGames.jl

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

## EFChaos.jl

I am currently working on turning [EFChaos](https://cendef.uva.nl/software/ef-chaos/ef-chaos.html) into a Julia package, relying on `DynamicalSystems.jl`. We are using Julia more and more for teaching and research, so it makes sense to invest some time in making it more accessible. 

## FRED_MD

Import and transform the [FRED](https://research.stlouisfed.org/wp/more/2015-012) monthly data. See [here](https://s3.amazonaws.com/files.fred.stlouisfed.org/fred-md/Appendix_Tables_Update.pdf) for a variable description


#### Installing

For now I am not going to publish it on PyPI. If you want to use it in the meantime simply do,

```bash
pip install git+https://github.com/NoFishLikeIan/fred_md
```

should do the trick.

#### Usage

The transformations are the suggested ones, taken from [McCracken, 2015](https://s3.amazonaws.com/real.stlouisfed.org/wp/2015/2015-012.pdf).

You can get the raw and the transformed data as,


```python
from fred_md.ingest_fred import import_transformed_data, import_raw_data

df = import_transformed_data()
raw_df = import_raw_data()
```

The package defaults to the latest version. If you want a specific one, just imput the version as `YYYY-MM`, 


```python
from fred_md.ingest_fred import import_transformed_data, import_raw_data

df = import_transformed_data("2018-02")
raw_df = import_raw_data("2018-02")
```

