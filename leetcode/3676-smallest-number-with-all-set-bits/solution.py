class Solution:
    def smallestNumber(self, n: int) -> int:
        # Count the number of bits in the binary representation of n
        num_bits = n.bit_length()
        
        # Create a number with all bits set: 2^num_bits - 1
        all_set_bits = (1 << num_bits) - 1
        
        # If all_set_bits is less than n, shift left one more bit and set all bits
        if all_set_bits < n:
            num_bits += 1
            all_set_bits = (1 << num_bits) - 1
        
        return all_set_bits