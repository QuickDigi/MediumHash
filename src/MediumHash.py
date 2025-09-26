import struct

from utils import avalanche_function, rotate_left, rotate_right
from utils.non_linear_transform import non_linear_transform

class MediumHash:
    def __init__(self):
        # Initial constants based on mathematical constants and primes
        with open('hash/g_is.bin', 'rb') as file:
            data = file.read()
            # 'Q' = 64-bit unsigned, '>Q' = big-endian
            self.initial_state = list(struct.unpack(f'>{len(data)//8}Q', data))
        
        # Round constants for added security
        with open('hash/g_rc.bin', 'rb') as file:
            data = file.read()
            self.round_constants = list(struct.unpack(f'>{len(data)//8}Q', data))

    def pre_process(self, data):
        """Advanced preprocessing with padding and length encoding"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Add custom padding scheme
        bit_len = len(data) * 8
        data += b'\x80'  # Add single bit '1'
        
        # Pad until length ≡ 448 (mod 512)
        while (len(data) % 64) != 56:
            data += b'\x00'
        
        # Append original length as 64-bit big-endian
        data += struct.pack('>Q', bit_len)
        
        return data
    
    def sponge_absorb(self, state, block):
        """Sponge construction absorption phase"""
        for i in range(8):
            if i * 8 < len(block):
                chunk = block[i*8:(i+1)*8].ljust(8, b'\x00')
                value = struct.unpack('<Q', chunk)[0]
                state[i] ^= value
        return state
    
    def permutation_round(self, state, round_num):
        """Advanced permutation function with multiple transformations"""
        new_state = state.copy()
        
        # Phase 1: Non-linear mixing
        for i in range(8):
            a = state[i]
            b = state[(i + 1) % 8]
            c = state[(i + 2) % 8]
            
            # Apply non-linear transformation
            new_state[i] = non_linear_transform(a, b, c)
            new_state[i] ^= self.round_constants[round_num % len(self.round_constants)]
        
        # Phase 2: Diffusion with rotation
        for i in range(8):
            new_state[i] = rotate_left(new_state[i], (i * 7 + round_num) % 64)
            new_state[i] ^= rotate_right(new_state[(i + 4) % 8], (i * 11 + round_num) % 64)
        
        # Phase 3: Avalanche effect
        for i in range(8):
            new_state[i] = avalanche_function(new_state, i)
        
        # Phase 4: Cross-state mixing
        for i in range(8):
            temp = new_state[i]
            temp ^= new_state[(i + 3) % 8] >> 17
            temp ^= new_state[(i + 5) % 8] << 23
            temp = (temp * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
            new_state[i] = temp
        
        return new_state
    
    def hash(self, data, rounds=64, output_size=512):
        """Main hashing function with configurable parameters"""
        # Initialize state
        state = self.initial_state.copy()
        
        # Preprocess input
        processed_data = self.pre_process(data)
        
        # Process in 512-bit blocks
        for i in range(0, len(processed_data), 64):
            block = processed_data[i:i+64]
            
            # Absorb block into state
            state = self.sponge_absorb(state, block)
            
            # Apply permutation rounds
            for round_num in range(rounds):
                state = self.permutation_round(state, round_num)
        
        # Final mixing rounds for security
        for final_round in range(8):
            state = self.permutation_round(state, final_round + 1000)
        
        # Generate output hash
        if output_size == 256:
            return ''.join([f"{state[i]:016x}" for i in range(4)])
        elif output_size == 512:
            return ''.join([f"{state[i]:016x}" for i in range(8)])
        else:
            # Custom output size
            output = ''.join([f"{state[i]:016x}" for i in range(8)])
            return output[:output_size // 4]
