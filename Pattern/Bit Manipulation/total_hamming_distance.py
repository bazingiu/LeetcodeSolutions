from typing import List

class Solution:
    """
    A class used to calculate the total Hamming distance between all pairs of integers in a list.
    sol.totalHammingDistance([4, 14, 2]) -> 6
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0  # Initialize the total Hamming distance to 0
        for i in range(32):  # Iterate over each bit position (0 to 31)
            ones = sum((num >> i) & 1 for num in nums)  # Count the number of 1s at the i-th bit position
            zeros = len(nums) - ones  # Calculate the number of 0s at the i-th bit position
            ans += ones * zeros  # Add the product of ones and zeros to the total Hamming distance
        return ans  # Return the total Hamming distance

"""    
    Explanation
    -----------
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    For the given example [4, 14, 2]:
    - Binary representations: 4 -> 0100, 14 -> 1110, 2 -> 0010
    - Pairwise Hamming distances:
      - Hamming distance between 4 and 14: 2 (0100 vs 1110)
      - Hamming distance between 4 and 2: 2 (0100 vs 0010)
      - Hamming distance between 14 and 2: 2 (1110 vs 0010)
    - Total Hamming distance: 2 + 2 + 2 = 6

    The function works by iterating over each bit position (0 to 31) and counting the number of 1s and 0s at each position.
    The product of the number of 1s and 0s at each bit position gives the contribution to the total Hamming distance for that bit position.
    Summing these contributions for all bit positions gives the total Hamming distance.
"""