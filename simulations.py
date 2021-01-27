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
for n in range(1, 11):
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
max_cdf = np.empty((10, s))
max_pmf = np.empty((10, s))

for n in range(1, 11):
    max_cdf[(n - 1), :] = cdf ** n
    max_pmf[(n - 1), 0] = max_cdf[(n - 1), 0]
    max_pmf[(n - 1), 1:] = max_cdf[(n - 1), 1:] - max_cdf[(n - 1), :-1]

# Chain model
# A -> B -> C
n = 4
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
distD_C = pm.ConditionalProbabilityTable(cpd, [distC_B])

A = pm.Node(distA, name="A")
B = pm.Node(distB_A, name="B")
C = pm.Node(distC_B, name="C")
D = pm.Node(distD_C, name="D")

model = pm.BayesianNetwork("Chain Model")
model.add_states(A, B, C, D)
model.add_edge(A, B)
model.add_edge(B, C)
model.add_edge(C, D)
model.bake()

model.predict_proba([[None, None, None, None]])

# Star model
# A  B
#  \/
#  C
n = 3
t = s - 3
distA = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})
distB = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})
distC = pm.DiscreteDistribution({"F": max_cdf[n - 1, t], "S": 1 - max_cdf[n - 1, t]})

cpd = [
    ["F", "F", "F", "F", max_cdf[n - 1, t]],
    ["F", "F", "F", "S", 1 - max_cdf[n - 1, t]],
    ["F", "F", "S", "F", max_cdf[n, t]],
    ["F", "F", "S", "S", 1 - max_cdf[n, t]],
    ["F", "S", "F", "F", max_cdf[n, t]],
    ["F", "S", "F", "S", 1 - max_cdf[n, t]],
    ["F", "S", "S", "F", max_cdf[n + 1, t]],
    ["F", "S", "S", "S", 1 - max_cdf[n + 1, t]],
    ["S", "F", "F", "F", max_cdf[n, t]],
    ["S", "F", "F", "S", 1 - max_cdf[n, t]],
    ["S", "F", "S", "F", max_cdf[n + 1, t]],
    ["S", "F", "S", "S", 1 - max_cdf[n + 1, t]],
    ["S", "S", "F", "F", max_cdf[n + 1, t]],
    ["S", "S", "F", "S", 1 - max_cdf[n + 1, t]],
    ["S", "S", "S", "F", max_cdf[n + 2, t]],
    ["S", "S", "S", "S", 1 - max_cdf[n + 2, t]],
]

distD_ABC = pm.ConditionalProbabilityTable(cpd, [distA, distB, distC])

A = pm.Node(distA, name="A")
B = pm.Node(distB, name="B")
C = pm.Node(distC, name="C")
D = pm.Node(distD_ABC, name="D")

model = pm.BayesianNetwork("Tree Model")
model.add_states(A, B, C, D)
model.add_edge(A, D)
model.add_edge(B, D)
model.add_edge(C, D)
model.bake()

model.predict_proba([[None, None, None, None]])
