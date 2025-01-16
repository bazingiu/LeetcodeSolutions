from basic_bit_operations import check_bit, set_bit, reset_bit, flip_bit
from advanced_bit_operations import extract_bits, set_multiple_bits
from bit_analysis import pop_count, power_of_two, find_msb, find_lsb

# Example usage:
if __name__ == "__main__":
    n = 0b10110
    mask = 0b00100
    print("Check bit:", check_bit(n, mask))  # Output: True

    n = 0b10100
    mask = 0b00010
    print("Set bit:", bin(set_bit(n, mask)))  # Output: 0b10110

    n = 0b10110
    mask = 0b11101
    print("Reset bit:", bin(reset_bit(n, mask)))  # Output: 0b10100

    n = 0b10110
    mask = 0b00010
    print("Flip bit:", bin(flip_bit(n, mask)))  # Output: 0b10100

    n = 0b101110
    mask = 0b001100
    print("Extract bits:", bin(extract_bits(n, mask, 2)))  # Output: 0b11

    n = 0b1001
    mask = 0b0110
    print("Set multiple bits:", bin(set_multiple_bits(n, mask)))  # Output: 0b1111

    n = 0b101110
    print("Pop count:", pop_count(n))  # Output: 4

    n = 0b10000
    print("Power of two:", power_of_two(n))  # Output: True

    n = 0b101110
    print("Find MSB:", find_msb(n))  # Output: 5

    n = 0b101110
    print("Find LSB:", find_lsb(n))  # Output: 1