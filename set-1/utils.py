def hamming_distance(a, b):
    """Return the Hamming distance of two strings of equal length."""

    if len(a) != len(b):
        print "Error: strings must be of the same length."
        ret = abs(len(a) - len(b))
        exit(ret)

    hamm = 0

    for x, y in zip(a, b):
        d = ord(x) ^ ord(y)
        while d > 0:
            hamm += d & 1
            d >>= 1
    return hamm


def xor_strings(a, b):
    """xor strings"""
    if len(a) == len(b):
        res = ''
        for i in range(len(a)):
            res = res + xor_byte(a[i], b[i])
    return res


def xor_byte(a, b):
    """bytewise xor"""
    return chr(ord(a) ^ ord(b))


def letter_count(text, filter):
    """Return count of filter letters in text"""
    n = 0
    for t in text.lower():
        if t in filter:
            n += 1
    return n
