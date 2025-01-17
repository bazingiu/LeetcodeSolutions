# Count the number of bits set to 1 (pop count)
def pop_count(n):
    """
    Counts the number of bits set to 1 in n.
    Returns: The count.
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Check if a number is a power of 2
def power_of_two(n):
    """
    Checks if n is a power of two.
    Returns: True if n is a power of two, otherwise False.
    """
    return (n & (n - 1)) == 0 and n != 0

# Find the most significant bit (MSB)
def find_msb(n):
    """
    Finds the position of the most significant bit (MSB) in n.
    Returns: The 0-based index of the MSB.
    """
    msb = 0
    while n > 1:
        n >>= 1
        msb += 1
    return msb

# Find the least significant bit (LSB)
def find_lsb(n):
    """
    Finds the position of the least significant bit (LSB) in n.
    Returns: The 0-based index of the LSB.
    """
    return (n & -n).bit_length() - 1

#find n * 2^K
def mult_by_power_of_two(n, power):
    """
    Multiply a number by a power of two.
    Returns: The result of the multiplication.
    """
    return n << power

# find n / 2^K
def div_by_power_of_two(n, power):
    """
    Divide a number by a power of two.
    Returns: The result of the division.
    """
    return n >> power

# fing X %  2^K
def mod_by_power_of_two(n, power):
    """
    Find the modulo of a number by a power of two.
    Returns: The result of the modulo operation.
    """
    return n & (power - 1)
