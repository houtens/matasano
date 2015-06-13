#!/usr/bin/env python

def pkcs7_encode(text, key=16):
    """Apply PKCS#7 padding"""
    l = len(text)
    x = key - (l % key)
    return str(text + bytearray([x] * x))

message = "YELLOW SUBMARINE"

p = pkcs7_encode(message, 20)
print p.encode('hex')
