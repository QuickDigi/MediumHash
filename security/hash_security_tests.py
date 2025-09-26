import random, statistics

def to_hex(val: bytes | str | int) -> str:
    if isinstance(val, bytes):
        return val.hex()
    elif isinstance(val, str):
        try:
            int(val, 16)
            return val
        except ValueError:
            return val.encode().hex()
    elif isinstance(val, int):
        return val.to_bytes((val.bit_length() + 7) // 8, "big").hex()
    return str(val).encode().hex()

def hamming_distance(a: str, b: str) -> int:
    a_bin = bin(int(a, 16))[2:].zfill(len(a) * 4)
    b_bin = bin(int(b, 16))[2:].zfill(len(b) * 4)
    return sum(ch1 != ch2 for ch1, ch2 in zip(a_bin, b_bin))

def avalanche_test(hasher, rounds: int = 200, msg_len: int = 32):
    print("\n=== Avalanche Test ===")
    distances = []
    for _ in range(rounds):
        msg = bytearray(random.getrandbits(8) for _ in range(msg_len))
        h1 = to_hex(hasher.hash(msg))

        # flip 1 random bit
        bit = random.randrange(msg_len * 8)
        msg[bit // 8] ^= 1 << (bit % 8)

        h2 = to_hex(hasher.hash(msg))
        dist = hamming_distance(h1, h2)
        distances.append(dist / (len(h1) * 4))

    print(f"Avalanche avg = {statistics.mean(distances)*100:.2f}%")
    print(f"Std dev       = {statistics.stdev(distances)*100:.2f}%")

def collision_test(hasher, rounds: int = 5000, msg_len: int = 16):
    print("\n=== Collision Test ===")
    seen = set()
    collisions = 0

    for i in range(rounds):
        msg = bytes(random.getrandbits(8) for _ in range(msg_len))
        h = to_hex(hasher.hash(msg))

        if h in seen:
            collisions += 1
        else:
            seen.add(h)

        if (i + 1) % (rounds // 10) == 0:
            print(f"Progress: {i + 1}/{rounds}")

    print(f"\nTotal tested = {rounds}")
    print(f"Collisions   = {collisions}")
    if collisions == 0:
        print("✅ No collisions found (good sign).")
    else:
        print("⚠️ Collisions detected!")

def distribution_test(hasher, rounds: int = 2000, msg_len: int = 16):
    print("\n=== Distribution Test ===")
    counts = [0] * 256
    for _ in range(rounds):
        msg = bytes(random.getrandbits(8) for _ in range(msg_len))
        h = to_hex(hasher.hash(msg))
        b = bytes.fromhex(h)
        for byte in b:
            counts[byte] += 1

    mean = statistics.mean(counts)
    stdev = statistics.stdev(counts)
    print(f"Mean freq = {mean:.2f}, Std dev = {stdev:.2f}")
