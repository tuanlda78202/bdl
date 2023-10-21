#! /usr/bin/env python3
import sys

N = 10000
current_k = None
sum_k = 0

for line in sys.stdin:
    # Split the input into key (k) and value (xi)
    k, xi = int(line.strip().split("\t")[0]), int(line.strip("\t").split()[1])

    # Reduce phase: Accumulate xi for each key k
    if current_k == k:
        sum_k += xi
    else:
        if current_k is not None:
            # Output the sum_k for the current key
            print(f"0\t{sum_k}")
        current_k = k
        sum_k = xi

# Output the final sum_k for the last key
if current_k is not None:
    print(f"0\t{sum_k}")
