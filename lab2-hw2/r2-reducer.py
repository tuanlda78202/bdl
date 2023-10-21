#! /usr/bin/env python3
import sys

N = 10000
total_sum = 0

for line in sys.stdin:
    # Split the input into key (k) and value (sumk)
    _, sumk = int(line.strip().split("\t")[0]), int(line.strip().split("\t")[1])

    # Accumulate the sum and count for each key k
    total_sum += sumk

# Calculate the mean
mean = total_sum / N
print(f"Mean: {mean}")
