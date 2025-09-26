def rotate_left(x, n, bits=64):
    """Rotate bits to the left"""
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)