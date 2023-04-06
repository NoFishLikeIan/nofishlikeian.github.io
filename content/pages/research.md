Title: Research 📚
Date: 2023-04-06
Authors: Andrea Titton

# Economics

## Supply chain fragility

<figure style="float: right; text-align: center;">
    <img src="{static}/images/welfare_gain.png" alt="drawing" width="400"/>
    <figcaption>Welfare losses in endogenous production<br> network with unobservability</figcaption>
</figure>

I investigates the role of supply chain unobservability in generating endogenously fragile production networks. I study a simple production game in which firms need to pick suppliers by forming rational beliefs about to what extent their risk is correlated. After some math involving powers of the beta distribution, I find the optimal sourcing strategy of the agents and show that the network is fragile if and only if the correlation between the firms' risk is below a certain threshold. 
Finally, I characterise the propagation of risk across the production network and show that there are large and discontinuous welfare losses associated with the competitive equilibrium. 

## Social Cost of Carbon under Tipping points

I study the social cost of carbon (SCC) in a model with tipping points. I show that the SCC is a decreasing function of the probability of a tipping point, and that the SCC is zero if the probability of a tipping point is zero. I also show that the SCC is increasing in the elasticity of the damage function with respect to the temperature.

For example, assume temperature $T$ is a function of the emissions $E$ as 

$$
\text{d}T = -c \mu(T, E) \text{d}t + \sigma \text{d}W.
$$

where $\mu(T, E)$ is cubic in $T$ and linear $E$. Furthermore, assume a concave utility of emissions $u(E)$ and a convex damage function $d(T)$. Then a carbon tax reduces the risk of a path that leads to a tipping point (solid red line in the figure below).

<figure style="text-align: center;">
    <img src="{static}/images/carbon-tax.png" alt="drawing" width="900"/>
</figure>

Finally, I introduce a differential game where multiple emitters and a regulator interact. I show that the regulator can mitigate the probability of a tipping point by setting an optimal carbon tax.



## ETS prices and electricity market volatility

I study theoretically the impact of the volatility of the electricity market on ETS prices and firms green investments. **Work in Progress**

# Neuroscience
## Motion Perception and Particle Filters

To accurately estimate the position of a moving object, the brain must overcome neural processing delays. This is theorized to be achieved through motion extrapolation, a process in which information about an object’s previous trajectory is used to estimate its current position. Previous research has demonstrated that motion extrapolation can be modelled as Bayesian inference. In the present paper, we employ a particle filter to investigate whether this Bayesian framework can explain a recently discovered visual illusion, in which the perceived offset of a moving object is mislocalised forwards due to the presentation of dynamic noise. Preliminary results suggest that the model can capture this effect, and, therefore, that the illusion might be driven by motion extrapolation.

# Law and Finance
## NLP analysis and sustainability 

This is a joint work with the [Amsterdam Center for Law and Economics](https://acle.uva.nl/), partly funded by the [*A Sustainable Future*](https://asf.uva.nl/) grant.

Institutional investors have large voting power in many polluting firms. However, their engagement with portfolio companies is imperfectly observable. We infer it based on an NLP algorithm applied to investors' disclosures. We calculate the index for investors and study its relationship with CO2 emissions and ESG performance of portfolio companies.