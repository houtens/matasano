#!/usr/bin/env python
from utils import xor_strings

raw1 = "1c0111001f010100061a024b53535009181c"
raw2 = "686974207468652062756c6c277320657965"

r1 = raw1.decode('hex')
r2 = raw2.decode('hex')

print xor_strings(r1, r2).encode('hex')
