def reverseBits(self, n):
    """
    Reverses the bits of a given 32-bit unsigned integer.

    Args:
        n (int): A 32-bit unsigned integer.

    Returns:
        int: The 32-bit unsigned integer resulting from reversing the bits of the input.

    Time Complexity: O(1) - The loop runs a fixed number of times (32 iterations).
    Space Complexity: O(1) - Only a constant amount of extra space is used.
    """
    res = 0
    for i in range(32):
        # Extract the i-th bit from n and shift it to the correct position
        bit = (n >> i) & 1
        res += (bit << (31 - i))
    return res

# Example usage:
# Input:  43261596 (00000010100101000001111010011100 in binary)
# Output: 964176192 (00111001011110000010100101000000 in binary)
