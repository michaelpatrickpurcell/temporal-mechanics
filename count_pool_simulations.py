import numpy as np
import pomegranate as pm
from scipy.stats import binom

# =============================================================================
# Non-exploding Dice
# =============================================================================

N = 11
p = 1.0/2.0
pmf = np.array([[binom.pmf(k, n, p) for k in range(N)] for n in range(N)])
cdf = np.array([[binom.cdf(k, n, p) for k in range(N)] for n in range(N)])
sf = np.array([[binom.sf(k, n, p) for k in range(-1,N)] for n in range(N)])

# Chain model
# A -> B -> C
n = 5
t = 4

ppd_A = {
    "S": sf[n, t-2],
    "F": 1 - sf[n, t-2],
}
dist_A = pm.DiscreteDistribution(ppd_A)

cpd_B_A = [
    ["S", "S", sf[n+1, t-1]],
    ["S", "F", 1 - sf[n+1, t-1]],
    ["F", "S", sf[n, t-1]],
    ["F", "F", 1 - sf[n, t-1]],
]

dist_B_A = pm.ConditionalProbabilityTable(cpd_B_A, [dist_A])

cpd_C_B = [
    ["S", "S", sf[n+1, t]],
    ["S", "F", 1 - sf[n+1, t]],
    ["F", "S", sf[n, t]],
    ["F", "F", 1 - sf[n, t]],
]

dist_C_B = pm.ConditionalProbabilityTable(cpd_C_B, [dist_B_A])

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B_A, name="B")
C = pm.Node(dist_C_B, name="C")

model = pm.BayesianNetwork("Chain Model")
model.add_states(A, B, C)
model.add_edge(A, B)
model.add_edge(B, C)
model.bake()

model.predict_proba([[None, None, None]])
model.predict_proba([[None, "S", None]])

# Tree model
# A  B
#  \/
#  C
n = 5
t = 4

ppd_A = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_A = pm.DiscreteDistribution(ppd_A)

ppd_B = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_B = pm.DiscreteDistribution(ppd_B)

cpd_C_AB = [
    ["S", "S", "S", sf[n+2, t]],
    ["S", "S", "F", 1 - sf[n+2, t]],
    ["S", "F", "S", sf[n+1, t]],
    ["S", "F", "F", 1 - sf[n+1, t]],
    ["F", "S", "S", sf[n+1, t]],
    ["F", "S", "F", 1 - sf[n+1, t]],
    ["F", "F", "S", sf[n, t]],
    ["F", "F", "F", 1 - sf[n, t]],
]

dist_C_AB = pm.ConditionalProbabilityTable(cpd_C_AB, [dist_A, dist_B])

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B, name="B")
C = pm.Node(dist_C_AB, name="C")

model = pm.BayesianNetwork("Tree Model")
model.add_states(A, B, C)
model.add_edge(A, C)
model.add_edge(B, C)
model.bake()

model.predict_proba([[None, None, None]])
