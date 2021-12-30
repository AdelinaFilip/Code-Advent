import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

lines = [int(line.strip()) for line in lines]

# Part 1
count = 0

for i, measurement in enumerate(lines[:(len(lines) - 2)]):
    if measurement < lines[i+1]:
        count += 1

print(f"Part 1: {count}")

# Part 2
window_count = 0

if len(lines) < 4:
    window_count = 0

window_sum = sum(lines[:3])
for i in range(3, len(lines), 1):
    next_window_sum = window_sum - lines[i - 3] + lines[i]
    if next_window_sum > window_sum:
        window_count += 1
    
    window_sum = next_window_sum

print(f"Part 2: {window_count}")
