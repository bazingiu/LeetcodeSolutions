# Check a specific bit
def check_bit(n, mask):
    """
    Checks if a specific bit is set in n.
    Returns: True if the bit is set, otherwise False.
    """
    return (n & mask) != 0

# Set a specific bit to 1
def set_bit(n, mask):
    """
    Sets the specified bit to 1 in n.
    Returns: The modified number.
    """
    return n | mask

# Reset (set to 0) a specific bit
def reset_bit(n, mask):
    """
    Resets (sets to 0) the specified bit in n.
    Returns: The modified number.
    """
    return n & mask

# Flip (invert) a specific bit
def flip_bit(n, mask):
    """
    Inverts the specified bit in n.
    Returns: The modified number.
    """
    return n ^ mask