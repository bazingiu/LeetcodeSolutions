# Extract desired bits
def extract_bits(n, mask, shift):
    """
    Extracts specific bits from n as defined by the mask, then shifts them.
    Parameters:
    - n: The number from which to extract bits.
    - mask: A bitmask that specifies which bits to extract.
    - shift: The number of positions to shift the extracted bits to the right.
    
    Returns: The extracted bits.
    
    Example:
    If n = 0b11011010 (218 in decimal), mask = 0b00001111 (15 in decimal), and shift = 2,
    the function will extract the last 4 bits (0b1010) and then shift them 2 positions to the right,
    resulting in 0b0010 (2 in decimal).
    """
    return (n & mask) >> shift

# Set multiple bits at once
def set_multiple_bits(n, mask):
    """
    Sets multiple bits at once in n using the mask.
    Parameters:
    - n: The original number.
    - mask: A bitmask that specifies which bits to set.
    
    Returns: The modified number with the specified bits set.
    
    Example:
    If n = 0b11011010 (218 in decimal) and mask = 0b00000101 (5 in decimal),
    the function will set the bits specified by the mask, resulting in 0b11011111 (223 in decimal).
    """
    return n | mask

# swap 2 numbers x and y without using a temporary variable
def swap_numbers(x, y):
    """
    Swaps two numbers x and y without using a temporary variable.
    Parameters:
    - x: The first number.
    - y: The second number.
    
    Returns: The tuple (x, y) with the values swapped.
    
    Example:
    If x = 2 and y = 5, the function will return (5, 2).
    x = 2 ^ 5 = 7 (011 ^ 101 = 110) {x = x^y, y = y}
    y = 7 ^ 5 = 2 (110 ^ 101 = 011) {x = x^y, y = x^y^y = x}
    x = 7 ^ 2 = 5   (110 ^ 011 = 101) {x= x^y^x=y, y = x}
    """
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y