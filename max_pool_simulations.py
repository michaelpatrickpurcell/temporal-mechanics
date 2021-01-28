import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

s = 10
n = 4

TRIALS = 2 ** 16

pools = np.random.randint(s, size=(TRIALS, n))
results = np.max(pools, axis=1)
counts = sorted(Counter(results).items())

column_names = ["Result", "Probability"]
column_values = list(zip(*counts))
df = pd.DataFrame({k: v for k, v in zip(column_names, column_values)})
df["Probability"] /= TRIALS
print(df)

df.plot(x="Result", kind="bar", rot=0)
plt.show()

TRIALS = 2 ** 16
df = pd.DataFrame(
    columns=["t = %i" % t for t in range(s)], index=["n = %i" % n for n in range(1, 11)]
)
for n in range(1, 21):
    pools = np.random.randint(s, size=(TRIALS, n))
    results = np.max(pools, axis=1)
    probs = np.array([(results >= t).mean() for t in range(s)])
    df.loc["n = %i" % n] = probs

print(df)

# ========================================================================================
import itertools
import pomegranate as pm

s = 10
pmf = np.ones(s) / s
cdf = np.cumsum(pmf)
max_cdf = np.empty((20, s))
max_pmf = np.empty((20, s))

for n in range(1, 21):
    max_cdf[(n - 1), :] = cdf ** n
    max_pmf[(n - 1), 0] = max_cdf[(n - 1), 0]
    max_pmf[(n - 1), 1:] = max_cdf[(n - 1), 1:] - max_cdf[(n - 1), :-1]

sf = np.column_stack([np.zeros(20), 1 - max_cdf])

# Chain model
# A -> B -> C
n = 6
t = s - 3
distA = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})

cpd = [
    ["F", "F", max_cdf[n - 1, t]],
    ["F", "S", 1 - max_cdf[n - 1, t]],
    ["S", "F", max_cdf[n, t]],
    ["S", "S", 1 - max_cdf[n, t]],
]

distB_A = pm.ConditionalProbabilityTable(cpd, [distA])
distC_B = pm.ConditionalProbabilityTable(cpd, [distB_A])
# distD_C = pm.ConditionalProbabilityTable(cpd, [distC_B])

A = pm.Node(distA, name="A")
B = pm.Node(distB_A, name="B")
C = pm.Node(distC_B, name="C")
# D = pm.Node(distD_C, name="D")

model = pm.BayesianNetwork("Chain Model")
model.add_states(A, B, C)#, D)
model.add_edge(A, B)
model.add_edge(B, C)
# model.add_edge(C, D)
model.bake()

model.predict_proba([[None, None, None]])#, None]])

# Star model
# A  B
#  \/
#  C
n = 6
t = s - 3
distA = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})
distB = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})
#distC = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})

cpd = [
    ["F", "F", "F", max_cdf[n - 1, t]],
    ["F", "F", "S", 1 - max_cdf[n - 1, t]],
    ["F", "S", "F", max_cdf[n, t]],
    ["F", "S", "S", 1 - max_cdf[n, t]],
    ["S", "F", "F", max_cdf[n, t]],
    ["S", "F", "S", 1 - max_cdf[n, t]],
    ["S", "S", "F", max_cdf[n + 1, t]],
    ["S", "S", "S", 1 - max_cdf[n + 1, t]]]


# cpd = [
#     ["F", "F", "F", "F", max_cdf[n - 1, t]],
#     ["F", "F", "F", "S", 1 - max_cdf[n - 1, t]],
#     ["F", "F", "S", "F", max_cdf[n, t]],
#     ["F", "F", "S", "S", 1 - max_cdf[n, t]],
#     ["F", "S", "F", "F", max_cdf[n, t]],
#     ["F", "S", "F", "S", 1 - max_cdf[n, t]],
#     ["F", "S", "S", "F", max_cdf[n + 1, t]],
#     ["F", "S", "S", "S", 1 - max_cdf[n + 1, t]],
#     ["S", "F", "F", "F", max_cdf[n, t]],
#     ["S", "F", "F", "S", 1 - max_cdf[n, t]],
#     ["S", "F", "S", "F", max_cdf[n + 1, t]],
#     ["S", "F", "S", "S", 1 - max_cdf[n + 1, t]],
#     ["S", "S", "F", "F", max_cdf[n + 1, t]],
#     ["S", "S", "F", "S", 1 - max_cdf[n + 1, t]],
#     ["S", "S", "S", "F", max_cdf[n + 2, t]],
#     ["S", "S", "S", "S", 1 - max_cdf[n + 2, t]],
# ]

distC_AB = pm.ConditionalProbabilityTable(cpd, [distA, distB])

#distD_ABC = pm.ConditionalProbabilityTable(cpd, [distA, distB, distC])

A = pm.Node(distA, name="A")
B = pm.Node(distB, name="B")
C = pm.Node(distC_AB, name="C")
#D = pm.Node(distD_ABC, name="D")

model = pm.BayesianNetwork("Tree Model")
model.add_states(A, B, C)#, D)
model.add_edge(A, C)
model.add_edge(B, C)
#model.add_edge(C, D)
model.bake()

model.predict_proba([[None, None, None]])

# =============================================================================
# Tree model 2
#   A
#   |
# B C D
#  \| |
# E F G
#  \|/
#   H

n = 2
t = 10

ppd_A = {
    "S": sf[n, t-9],
    "F": 1 - sf[n, t-9],
}
dist_A = pm.DiscreteDistribution(ppd_A)

ppd_B = {
    "S": sf[n, t-6],
    "F": 1 - sf[n, t-6],
}
dist_B = pm.DiscreteDistribution(ppd_B)


cpd_C_A = [
    ["S", "S", sf[n, t-7]],
    ["S", "F", 1 - sf[n, t-7]],
    ["F", "S", sf[n, t-6]],
    ["F", "F", 1 - sf[n, t-6]],
]
dist_C_A = pm.ConditionalProbabilityTable(cpd_C_A, [dist_A])

ppd_D = {
    "S": sf[n, t-6],
    "F": 1 - sf[n, t-6],
}
dist_D = pm.DiscreteDistribution(ppd_D)

ppd_E = {
    "S": sf[n, t-3],
    "F": 1 - sf[n, t-3],
}
dist_E = pm.DiscreteDistribution(ppd_E)

cpd_F_BC = [
    ["S", "S", "S", sf[n, t-7]],
    ["S", "S", "F", 1 - sf[n, t-7]],
    ["S", "F", "S", sf[n, t-5]],
    ["S", "F", "F", 1 - sf[n, t-5]],
    ["F", "S", "S", sf[n, t-5]],
    ["F", "S", "F", 1 - sf[n, t-5]],
    ["F", "F", "S", sf[n, t-3]],
    ["F", "F", "F", 1 - sf[n, t-3]],
]
dist_F_BC = pm.ConditionalProbabilityTable(cpd_F_BC, [dist_B, dist_C_A])

cpd_G_D = [
    ["S", "S", sf[n, t-5]],
    ["S", "F", 1 - sf[n, t-5]],
    ["F", "S", sf[n, t-3]],
    ["F", "F", 1 - sf[n, t-3]],
]
dist_G_D = pm.ConditionalProbabilityTable(cpd_G_D, [dist_D])

cpd_H_EFG = [
    ["S", "S", "S", "S", sf[n, t-9]],
    ["S", "S", "S", "F", 1 - sf[n, t-9]],
    ["S", "S", "F", "S", sf[n, t-6]],
    ["S", "S", "F", "F", 1 - sf[n, t-6]],
    ["S", "F", "S", "S", sf[n, t-6]],
    ["S", "F", "S", "F", 1 - sf[n, t-6]],
    ["S", "F", "F", "S", sf[n, t-3]],
    ["S", "F", "F", "F", 1 - sf[n, t-3]],
    ["F", "S", "S", "S", sf[n, t-6]],
    ["F", "S", "S", "F", 1 - sf[n, t-6]],
    ["F", "S", "F", "S", sf[n, t-3]],
    ["F", "S", "F", "F", 1 - sf[n, t-3]],
    ["F", "F", "S", "S", sf[n, t-3]],
    ["F", "F", "S", "F", 1 - sf[n, t-3]],
    ["F", "F", "F", "S", sf[n, t]],
    ["F", "F", "F", "F", 1 - sf[n, t]],
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
