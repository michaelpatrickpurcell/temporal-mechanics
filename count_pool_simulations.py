import numpy as np
import pomegranate as pm
from scipy.stats import binom, nbinom
from scipy.special import comb
from itertools import product

# =============================================================================
# Non-exploding Dice
# =============================================================================
N = 21
p = 1.0/2.0
pmf = np.array([[binom.pmf(k, n, p) for k in range(N)] for n in range(N)])
cdf = np.array([[binom.cdf(k, n, p) for k in range(N)] for n in range(N)])
sf = np.array([[binom.sf(k, n, p) for k in range(-1,N)] for n in range(N)])

# =============================================================================
# Exploding Dice!
# =============================================================================
def exploding_pmf(d, n, t, h):
    mult = ((t-1)**n)/(d**(n+h))
    accum = 0
    for k in range(0, max(h,n)+1):
        accum += (comb(n,k, exact=True) * comb(n+h-k-1, h-k, exact=True) * ((d*(d-t)/(t-1))**k))
    return mult * accum

N = 21
d = 6
t = 4
pmf = np.array([[exploding_pmf(d=d, n=n, t=t, h=h) for h in range(N)] for n in range(N)])
cdf = np.column_stack((np.zeros(N), np.cumsum(pmf, axis=1)))
sf = 1 - cdf

# -----------------------------------------------------------------------------
# Three check systems
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Four check systems
# -----------------------------------------------------------------------------
# Tree model
# A B C
#  \|/
#   D
n = 6
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

ppd_C = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_C = pm.DiscreteDistribution(ppd_C)

cpd_D_ABC = [
    ["S", "S", "S", "S", sf[n+3, t]],
    ["S", "S", "S", "F", 1 - sf[n+3, t]],
    ["S", "S", "F", "S", sf[n+2, t]],
    ["S", "S", "F", "F", 1 - sf[n+2, t]],
    ["S", "F", "S", "S", sf[n+2, t]],
    ["S", "F", "S", "F", 1 - sf[n+2, t]],
    ["S", "F", "F", "S", sf[n+1, t]],
    ["S", "F", "F", "F", 1 - sf[n+1, t]],
    ["F", "S", "S", "S", sf[n+2, t]],
    ["F", "S", "S", "F", 1 - sf[n+2, t]],
    ["F", "S", "F", "S", sf[n+1, t]],
    ["F", "S", "F", "F", 1 - sf[n+1, t]],
    ["F", "F", "S", "S", sf[n+1, t]],
    ["F", "F", "S", "F", 1 - sf[n+1, t]],
    ["F", "F", "F", "S", sf[n, t]],
    ["F", "F", "F", "F", 1 - sf[n, t]],
]

dist_D_ABC = pm.ConditionalProbabilityTable(cpd_D_ABC, [dist_A, dist_B, dist_C])

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B, name="B")
C = pm.Node(dist_C, name="C")
D = pm.Node(dist_D_ABC, name="D")
model = pm.BayesianNetwork("Tree Model")
model.add_states(A, B, C, D)
model.add_edge(A, D)
model.add_edge(B, D)
model.add_edge(C, D)
model.bake()

model.predict_proba([[None, None, None, None]])

model.predict_proba([["S", "S", "S", None]])
model.predict_proba([["F", "F", "F", None]])

# -----------------------------------------------------------------------------
# Eight check systems
# -----------------------------------------------------------------------------
# Tree model 1
#     A
#     |
# B C D
#  \| |
# E F G
#  \|/
#   H

n = 6
t = 4

ppd_A = {
    "S": sf[n, t-3],
    "F": 1 - sf[n, t-3],
}
dist_A = pm.DiscreteDistribution(ppd_A)

ppd_B = {
    "S": sf[n, t-2],
    "F": 1 - sf[n, t-2],
}
dist_B = pm.DiscreteDistribution(ppd_B)

ppd_C = {
    "S": sf[n, t-2],
    "F": 1 - sf[n, t-2],
}
dist_C = pm.DiscreteDistribution(ppd_C)

cpd_D_A = [
    ["S", "S", sf[n+1, t-2]],
    ["S", "F", 1 - sf[n+1, t-2]],
    ["F", "S", sf[n, t-2]],
    ["F", "F", 1 - sf[n, t-2]],
]
dist_D_A = pm.ConditionalProbabilityTable(cpd_D_A, [dist_A])

ppd_E = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_E = pm.DiscreteDistribution(ppd_E)

cpd_F_BC = [
    ["S", "S", "S", sf[n+2, t-1]],
    ["S", "S", "F", 1 - sf[n+2, t-1]],
    ["S", "F", "S", sf[n+1, t-1]],
    ["S", "F", "F", 1 - sf[n+1, t-1]],
    ["F", "S", "S", sf[n+1, t-1]],
    ["F", "S", "F", 1 - sf[n+1, t-1]],
    ["F", "F", "S", sf[n, t-1]],
    ["F", "F", "F", 1 - sf[n, t-1]],
]
dist_F_BC = pm.ConditionalProbabilityTable(cpd_F_BC, [dist_B, dist_C])

cpd_G_D = [
    ["S", "S", sf[n+1, t-1]],
    ["S", "F", 1 - sf[n+1, t-1]],
    ["F", "S", sf[n, t-1]],
    ["F", "F", 1 - sf[n, t-1]],
]
dist_G_D = pm.ConditionalProbabilityTable(cpd_G_D, [dist_D_A])

cpd_H_EFG = [
    ["S", "S", "S", "S", sf[n+3, t]],
    ["S", "S", "S", "F", 1 - sf[n+3, t]],
    ["S", "S", "F", "S", sf[n+2, t]],
    ["S", "S", "F", "F", 1 - sf[n+2, t]],
    ["S", "F", "S", "S", sf[n+2, t]],
    ["S", "F", "S", "F", 1 - sf[n+2, t]],
    ["S", "F", "F", "S", sf[n+1, t]],
    ["S", "F", "F", "F", 1 - sf[n+1, t]],
    ["F", "S", "S", "S", sf[n+2, t]],
    ["F", "S", "S", "F", 1 - sf[n+2, t]],
    ["F", "S", "F", "S", sf[n+1, t]],
    ["F", "S", "F", "F", 1 - sf[n+1, t]],
    ["F", "F", "S", "S", sf[n+1, t]],
    ["F", "F", "S", "F", 1 - sf[n+1, t]],
    ["F", "F", "F", "S", sf[n, t]],
    ["F", "F", "F", "F", 1 - sf[n, t]],
]
dist_H_EFG = pm.ConditionalProbabilityTable(cpd_H_EFG, [dist_E, dist_F_BC, dist_G_D])

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B, name="B")
C = pm.Node(dist_C, name="C")
D = pm.Node(dist_D_A, name="D")
E = pm.Node(dist_E, name="E")
F = pm.Node(dist_F_BC, name="F")
G = pm.Node(dist_G_D, name="G")
H = pm.Node(dist_H_EFG, name="H")

model = pm.BayesianNetwork("Tree Model 1")
model.add_states(A, B, C, D, E, F, G, H)
model.add_edge(A, D)
model.add_edge(B, F)
model.add_edge(C, F)
model.add_edge(D, G)
model.add_edge(E, H)
model.add_edge(F, H)
model.add_edge(G, H)
model.bake()

model.predict_proba([[None, None, None, None, None, None, None, None]])
model.predict_proba([[None, None, None, None, "S", "S", "S", None]])

# Tree model 2
#   A
#   |
# B C D
#  \| |
# E F G
#  \|/
#   H
# Here we assume that each check inherits one die from each child
# regardless of success or failure. This die represents the fact
# that such checks have more aspects available (those assigned during
# the children as well as the current encounter) which makes it easier
# create matches during play.

n = 4
t = 4

ppd_A = {
    "S": sf[n, t-3],
    "F": 1 - sf[n, t-3],
}
dist_A = pm.DiscreteDistribution(ppd_A)

ppd_B = {
    "S": sf[n, t-2],
    "F": 1 - sf[n, t-2],
}
dist_B = pm.DiscreteDistribution(ppd_B)


cpd_C_A = [
    ["S", "S", sf[n+1+1, t-2]],
    ["S", "F", 1 - sf[n+1+1, t-2]],
    ["F", "S", sf[n+1, t-2]],
    ["F", "F", 1 - sf[n+1, t-2]],
]
dist_C_A = pm.ConditionalProbabilityTable(cpd_C_A, [dist_A])

ppd_D = {
    "S": sf[n, t-2],
    "F": 1 - sf[n, t-2],
}
dist_D = pm.DiscreteDistribution(ppd_D)

ppd_E = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_E = pm.DiscreteDistribution(ppd_E)

cpd_F_BC = [
    ["S", "S", "S", sf[n+2+2, t-1]],
    ["S", "S", "F", 1 - sf[n+2+2, t-1]],
    ["S", "F", "S", sf[n+1+2, t-1]],
    ["S", "F", "F", 1 - sf[n+1+2, t-1]],
    ["F", "S", "S", sf[n+1+2, t-1]],
    ["F", "S", "F", 1 - sf[n+1+2, t-1]],
    ["F", "F", "S", sf[n+2, t-1]],
    ["F", "F", "F", 1 - sf[n+2, t-1]],
]
dist_F_BC = pm.ConditionalProbabilityTable(cpd_F_BC, [dist_B, dist_C_A])

cpd_G_D = [
    ["S", "S", sf[n+1+1, t-1]],
    ["S", "F", 1 - sf[n+1+1, t-1]],
    ["F", "S", sf[n+1, t-1]],
    ["F", "F", 1 - sf[n+1, t-1]],
]
dist_G_D = pm.ConditionalProbabilityTable(cpd_G_D, [dist_D])

cpd_H_EFG = [
    ["S", "S", "S", "S", sf[n+3+3, t]],
    ["S", "S", "S", "F", 1 - sf[n+3+3, t]],
    ["S", "S", "F", "S", sf[n+2+3, t]],
    ["S", "S", "F", "F", 1 - sf[n+2+3, t]],
    ["S", "F", "S", "S", sf[n+2+3, t]],
    ["S", "F", "S", "F", 1 - sf[n+2+3, t]],
    ["S", "F", "F", "S", sf[n+1+3, t]],
    ["S", "F", "F", "F", 1 - sf[n+1+3, t]],
    ["F", "S", "S", "S", sf[n+2+3, t]],
    ["F", "S", "S", "F", 1 - sf[n+2+3, t]],
    ["F", "S", "F", "S", sf[n+1+3, t]],
    ["F", "S", "F", "F", 1 - sf[n+1+3, t]],
    ["F", "F", "S", "S", sf[n+1+3, t]],
    ["F", "F", "S", "F", 1 - sf[n+1+3, t]],
    ["F", "F", "F", "S", sf[n+3, t]],
    ["F", "F", "F", "F", 1 - sf[n+3, t]],
]
dist_H_EFG = pm.ConditionalProbabilityTable(cpd_H_EFG, [dist_E, dist_F_BC, dist_G_D])

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B, name="B")
C = pm.Node(dist_C_A, name="C")
D = pm.Node(dist_D, name="D")
E = pm.Node(dist_E, name="E")
F = pm.Node(dist_F_BC, name="F")
G = pm.Node(dist_G_D, name="G")
H = pm.Node(dist_H_EFG, name="H")

model = pm.BayesianNetwork("Tree Model 2")
model.add_states(A, B, C, D, E, F, G, H)
model.add_edge(A, C)
model.add_edge(B, F)
model.add_edge(C, F)
model.add_edge(D, G)
model.add_edge(E, H)
model.add_edge(F, H)
model.add_edge(G, H)
model.bake()

model.predict_proba([[None, None, None, None, None, None, None, None]])
model.predict_proba([[None, None, None, None, "S", "S", "S", None]])
model.predict_proba([[None, None, None, None, "F", "F", "F", None]])

# Shallow Model
# Here we assume that each check inherits one die from each child
# regardless of success or failure. This die represents the fact
# that such checks have more aspects available (those assigned during
# the children as well as the current encounter) which makes it easier
# create matches during play.
n = 3
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

ppd_C = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_C = pm.DiscreteDistribution(ppd_C)

ppd_D = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_D = pm.DiscreteDistribution(ppd_D)

ppd_E = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_E = pm.DiscreteDistribution(ppd_E)

ppd_F = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_F = pm.DiscreteDistribution(ppd_F)

ppd_G = {
    "S": sf[n, t-1],
    "F": 1 - sf[n, t-1],
}
dist_G = pm.DiscreteDistribution(ppd_G)

cpd = []
for values in product(["S", "F"], repeat=8):
    s = (np.array(values[:-1]) == "S").sum()
    if values[-1] == "S":
        cpd.append(list(values) + [sf[n+s+7, t]])
    else:
        cpd.append(list(values)+ [1 - sf[n+s, t]])
dist_list = [dist_A, dist_B, dist_C, dist_D, dist_E, dist_F, dist_G]
dist_H_ABCDEFG = pm.ConditionalProbabilityTable(cpd, dist_list)

A = pm.Node(dist_A, name="A")
B = pm.Node(dist_B, name="B")
C = pm.Node(dist_C, name="C")
D = pm.Node(dist_D, name="D")
E = pm.Node(dist_E, name="E")
F = pm.Node(dist_F, name="F")
G = pm.Node(dist_G, name="G")
H = pm.Node(dist_H_ABCDEFG, name="H")

model = pm.BayesianNetwork("Shallow Model")
model.add_states(A, B, C, D, E, F, G, H)
model.add_edge(A, H)
model.add_edge(B, H)
model.add_edge(C, H)
model.add_edge(D, H)
model.add_edge(E, H)
model.add_edge(F, H)
model.add_edge(G, H)
model.bake()

model.predict_proba([[None, None, None, None, None, None, None, None]])
