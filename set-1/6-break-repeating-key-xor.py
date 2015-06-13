#!/usr/bin/env python
from utils import hamming_distance
from operator import itemgetter
from utils import xor_byte, letter_count

# Calculate normalised Hamming distance over this many key lengths
# Experiment with 2..20 to get the best estimate
sample_size = 12

# included from 3-single-byte-xor.py

def count_non_english_chars(text):
    """Return the count of non-English characters"""
    count = 0
    for x in text:
        # Anything other than lower, upper and standard English punctuation
        # is considered to be non-English
        if ord(x) < 32 or ord(x) > 126:
            count += 1 
        # But make an exception for TAB, LF and CR
        if ord(x) == 9 or ord(x) == 10 or ord(x) == 13:
            count -= 1
    return count

def vowel_letter_ratio(vowels, letters):
    """Return the ratio of vowels to consonants"""
    if letters > 0:
        return vowels / float(letters)
    return 0



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

best = min(hamm_scores.items(), key=itemgetter(1))[0]
#print best

rows = ['' for x in range(best)]
for i, t in enumerate(text):
    rows[i % best] += t

output_list = []

for i, raw in enumerate(rows):
    vowel_set = "aeiou"
    consonant_set = "bcdfghjklmnpqrstvwxyz"

    raw_length = len(raw)

    for idx in range(256):
        res = ""
        for key in raw:
            b = xor_byte(key, chr(idx))
            res += b

        eng = count_non_english_chars(res)

        space_freq = letter_count(res, " ") / float(raw_length)
        vowel_freq = letter_count(res, vowel_set) / float(raw_length)
        cons_freq = letter_count(res, consonant_set) / float(raw_length)

        # must be all printable English chars
        # must contain at least 30% consonants and 10% vowels
        # must contain 10% spaces
        if eng == 0 and cons_freq > 0.3 and vowel_freq > 0.10 and space_freq > 0.10:
            output_list.append(res)

if len(output_list) != best:
    print "Failed to find good English matches for all possible keys"
    exit(1)



# transpose the colums for output
rows = ['' for x in range(len(output_list[0]))]
for p in range(len(output_list)):
    for i, o in enumerate(output_list[p]):
        rows[i] += o

# We don't want to display newline or space separators so join the raw
# text before printing.
output = ""
for i, r in enumerate(rows):
    output += ''.join(r)

print output
