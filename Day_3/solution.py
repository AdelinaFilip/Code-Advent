import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

# Part 1
bins = np.array(lines)
bins = [binary.strip() for binary in bins]

counts = np.zeros(shape=(len(bins[0]), 2))

for binary in bins:
    for i, b in enumerate(binary):
        if b == '0':
            counts[i][0] += 1
        else:
            counts[i][1] += 1

gamma_rate = ['0' if np.max(v) == v[0] else '1' for v in counts]
g_rate = "".join(gamma_rate)

epsilon_rate = ['0' if np.min(v) == v[0] else '1' for v in counts]
e_rate = "".join(epsilon_rate)

result = int(g_rate,2) * int(e_rate, 2)
print(result)