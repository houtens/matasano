#!/usr/bin/env python
from utils import xor_byte

key = "ICE"
plain = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

ciphertext = ""
for x, r in enumerate(plain):
    ciphertext += xor_byte(r, key[x %3])

print ciphertext.encode('hex')
