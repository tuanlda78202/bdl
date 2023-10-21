#!/usr/bin/env python3
"""mapper.py"""

import sys

def read_input(file, kmer):
    # Ignore line start with >
    for line in file:
        line_clean = line.strip()
        if not line_clean.startswith(">"):
            try:
                yield [line_clean[i:i+kmer] for i in range(len(line_clean)-kmer+1)]
            except: 
                continue

def main(separator='\t'):
    if len(sys.argv) > 2:
        kmer = sys.argv[2]
    else:
        kmer = 9

    # input comes from STDIN (standard input)
    data = read_input(sys.stdin, kmer)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial    word count is 1
        for word in words:            
            print(f"{word}{separator}1")

if __name__ == "__main__":
    main()
