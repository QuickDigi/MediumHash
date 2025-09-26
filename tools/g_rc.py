# Round Constants
import random
import struct

random.seed(9041103497)

with open('../hash/g_rc.bin', 'wb') as file:
    for _ in range(122880):
        file.write(struct.pack('>Q', random.getrandbits(64)))
