#!/usr/bin/env python
from collections import Counter

# Assume the key is 16 bytes 
key_length = 16

with open("8.txt", "r") as f:
    lines = f.read().splitlines()

for idx, line in enumerate(lines):
    # Create a counter to enumerate occurances of each cipher block
    c = Counter()
    for x in range(0, len(line), key_length):
        c[ line[x:x+key_length] ] += 1

    # We could use most_common but the sorted counter is easier to work with
    sorted(c)

    for k, v in c.items():
        if v > 1:
            # Print only lines that contain repeated ciphertext blocks
            print idx, line
            break
