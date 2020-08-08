import csv
import random
from collections import Counter, defaultdict

import matplotlib.pyplot as plt

# This was written in a rush...PRs more than welcome! 🙏

# Setup
f = open('./data.csv')
reader = csv.reader(f)
dists = defaultdict(lambda: {str(d): 0 for d in range(1, 10)})
non_numerical_keys = ["createdAt", "updatedAt", "websiteUrl", "pushedAt"]  # Non numerical values
k2i = None

# Build first digit distributions, per key
for i, row in enumerate(reader):
    if i == 0:
        k2i = {k: j for j, k in enumerate(row)}
        continue
    for key in k2i.keys():
        key_idx = k2i[key]
        try:
            first_digit = str(row[key_idx][0])
            if first_digit.isdigit():
                dists[key][first_digit] += 1
            else:  # Not a numerical value, ignore next time
                non_numerical_keys.append(key)
        except (IndexError, KeyError):
            continue

# Plot distributions
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

for k, dist in dists.items():
    if k in non_numerical_keys:
        continue
    dist = dict(sorted(dist.items()))
    color = [random.random() for i  in range(3)]
    xvals = list(dist.keys())
    yvals = list(dist.values())
    ax.plot(xvals, yvals, color=color, label=k)

plt.legend(loc='upper right', prop={'size': 7})
plt.show()
