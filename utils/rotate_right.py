def rotate_right(x, n, bits=64):
    """Rotate bits to the right"""
    return ((x >> n) | (x << (bits - n))) & ((1 << bits) - 1)