import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

lines = [int(line.strip()) for line in lines]

# Part 1
count = 0

for i, measurement in enumerate(lines[:(len(lines) - 2)]):
    if measurement < lines[i+1]:
        count += 1

print(count)