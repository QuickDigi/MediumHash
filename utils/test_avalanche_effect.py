def test_avalanche_effect(hasher, base_input):
    """Test avalanche effect by flipping single bits"""
    base_hash = hasher.advanced_hash(base_input)
    
    print(f"Original input: '{base_input}'")
    print(f"Original hash:  {base_hash}")
    print("\nAvalanche test (single bit changes):")
    
    if isinstance(base_input, str):
        base_bytes = base_input.encode('utf-8')
    else:
        base_bytes = base_input
    
    for i in range(min(3, len(base_bytes) * 8)):  # first 3 bits
        # Flip a single bit
        modified_bytes = bytearray(base_bytes)
        byte_pos = i // 8
        bit_pos = i % 8
        modified_bytes[byte_pos] ^= (1 << bit_pos)
        
        modified_hash = hasher.advanced_hash(bytes(modified_bytes))
        
        # Count different bits
        diff_bits = bin(int(base_hash, 16) ^ int(modified_hash, 16)).count('1')
        diff_percentage = (diff_bits / (len(base_hash) * 4)) * 100
        
        print(f"Bit {i:2d} flipped: {modified_hash} (diff: {diff_bits:3d} bits, {diff_percentage:.1f}%)")
