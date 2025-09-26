from utils import rotate_left, rotate_right


def avalanche_function(state, index):
    """Creates avalanche effect for better diffusion"""
    temp = state[index]
    temp ^= rotate_left(temp, 7) ^ rotate_right(temp, 11)
    temp = (temp * 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    temp ^= temp >> 32
    return temp