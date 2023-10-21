#! /usr/bin/env python3
import sys

N = 10000

for line in sys.stdin:
    # Split the input into key (i) and value (xi)
    i, xi = int(line.strip().split()[0]), int(line.strip().split()[1])
    # Map phase: Output key-value pairs (k, xi)
    k = i % int(N**0.5)  # Calculate k as i mod √N
    print(f"{k}\t{xi}")
