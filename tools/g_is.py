# Initial State
import random
import struct

with open('../hash/g_is.bin', 'wb') as file:
    random.seed(42)
    
    for _ in range(122880):
        file.write(struct.pack('>Q', random.getrandbits(64)))
