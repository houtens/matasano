#!/usr/bin/env python
from utils import xor_byte, letter_count

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


# For reference: vowel frequency should be ~ 38%
raw_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
vowel_set = "aeiou"
consonant_set = "bcdfghjklmnpqrstvwxyz"
output_list = []

raw = raw_hex.decode('hex')
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

print output_list 

