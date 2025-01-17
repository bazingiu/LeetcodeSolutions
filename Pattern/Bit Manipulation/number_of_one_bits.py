def hammingWeight(self, n):
    """
    Calculate the number of '1' bits (Hamming weight) in the binary representation of an integer.

    Parameters:
    n (int): The integer whose Hamming weight is to be calculated.

    Returns:
    int: The number of '1' bits in the binary representation of the input integer.

    Time Complexity: O(k), where k is the number of bits in the integer.
    Space Complexity: O(1), as the space used does not depend on the input size.
    """
    res = 0
    while n: 
        if n & 1: 
            res += 1
        n = n >> 1
    return res  