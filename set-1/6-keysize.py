#!/usr/bin/env python
from utils import hamming_distance

# Calculate normalised Hamming distance over this many key lengths
# Experiment with 2..20 to get the best estimate
sample_size = 10

with open("6.txt", "r") as fp:
    raw_list = fp.read().splitlines()
    raw_text = ''.join(raw_list) 
# convert input text from base64 to plain
text = raw_text.decode('base64')

hamm_scores = {}

for b in range(2,41):
    # Split text into chunks of length b
    text_chunks = [text[x:x+b] for x in range(0,len(text),b)]
    # First chunk
    s1 = text_chunks[0]
    hamming_sum = 0 
    for block in range(1,sample_size):
        # Subsequent chunks
        s2 = text_chunks[block]
        d = hamming_distance(s1, s2)
        hamming_sum += d
    average_hamm = hamming_sum / float(sample_size)

    normalised_hamming_distance = average_hamm / float(b)
    hamm_scores[b] = normalised_hamming_distance
   

# Sort the scores with the lowest first - creates tuple of (length, normalised_hamming_distance)
sorted_hamm_scores = sorted(hamm_scores.iteritems(), key=lambda (k, v): (v, k))[0]
# Print the most likely key length
#print sorted_hamm_scores[0], sorted_hamm_scores[1]
print "best guess:", sorted_hamm_scores[0]

