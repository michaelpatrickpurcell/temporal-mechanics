import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

s = 10
n = 4

TRIALS = 2**16

pools = np.random.randint(s, size=(TRIALS, n))
results = np.max(pools, axis=1)
counts = sorted(Counter(results).items())

column_names = ["Result", "Probability"]
column_values = list(zip(*counts))
df = pd.DataFrame({k:v for k,v in zip(column_names, column_values)})
df["Probability"] /= TRIALS
print(df)

df.plot(x="Result", kind="bar", rot=0)
plt.show()

TRIALS = 2**16
df = pd.DataFrame(columns=["t = %i" % t for t in range(s)], index=["n = %i" % n for n in range(1,11)])
for n in range(1,11):
    pools = np.random.randint(s, size=(TRIALS, n))
    results = np.max(pools, axis=1)
    probs = np.array([(results >= t).mean() for t in range(s)])
    df.loc["n = %i" % n] = probs

print(df)

# ========================================================================================

import pomegranate as pm

s = 10
pmf = np.ones(s)/s
cdf = np.cumsum(pdf)
max_cdf = np.empty((10, s))
max_pmf = np.empty((10, s))

for n in range(1,11):
    max_cdf[(n-1),:] = cdf**n
    max_pmf[(n-1),0] = max_cdf[(n-1),0]
    max_pmf[(n-1),1:] = max_cdf[(n-1),1:] - max_cdf[(n-1),:-1]

print(max_cdf)
print()
print(max_pmf)
