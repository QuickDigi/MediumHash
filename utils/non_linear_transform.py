def non_linear_transform(x, y, z):
    """Non-linear transformation function"""
    return ((x & y) | ((~x) & z)) ^ (x & z) ^ (y | z)
