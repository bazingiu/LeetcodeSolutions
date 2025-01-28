from collections import defaultdict
from typing import List

class Solution:
    """
    This class provides a solution to the problem of finding the longest consecutive sequence in an unsorted array of integers.
    Methods
    
    Time Complexity
    O(n): The algorithm iterates through the list of numbers once.
    
    Space Complexity
    O(n): The algorithm uses a dictionary to store the length of sequences for each number.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        # Dictionary to store the length of the sequence that each number is part of
        num_to_sequence_length = defaultdict(int)
        # Variable to keep track of the maximum length of consecutive sequence found
        max_length = 0

        for num in nums:
            # If the number is not already part of a sequence
            if not num_to_sequence_length[num]:
                # Get the length of the sequence to the left of the current number
                left_length = num_to_sequence_length[num - 1]
                
                # Get the length of the sequence to the right of the current number
                right_length = num_to_sequence_length[num + 1]
                
                # Calculate the total length of the sequence including the current number
                current_length = left_length + right_length + 1

                # Update the length of the sequence for the current number
                num_to_sequence_length[num] = current_length
                # Update the length of the sequence for the boundary numbers of the sequence
                num_to_sequence_length[num - left_length] = current_length
                num_to_sequence_length[num + right_length] = current_length

                # Update the maximum length of consecutive sequence found
                max_length = max(max_length, current_length)

        return max_length

        # Step-by-step explanation:
        # 1. num = 100
        #    left_length = 0, right_length = 0, current_length = 1
        #    num_to_sequence_length = {100: 1}
        #    max_length = 1
        #
        # 2. num = 4
        #    left_length = 0, right_length = 0, current_length = 1
        #    num_to_sequence_length = {100: 1, 4: 1}
        #    max_length = 1
        #
        # 3. num = 200
        #    left_length = 0, right_length = 0, current_length = 1
        #    num_to_sequence_length = {100: 1, 4: 1, 200: 1}
        #    max_length = 1
        #
        # 4. num = 1
        #    left_length = 0, right_length = 0, current_length = 1
        #    num_to_sequence_length = {100: 1, 4: 1, 200: 1, 1: 1}
        #    max_length = 1
        #
        # 5. num = 3
        #    left_length = 1 (num_to_sequence_length[2]), right_length = 0, current_length = 2
        #    num_to_sequence_length = {100: 1, 4: 1, 200: 1, 1: 1, 3: 2, 2: 2}
        #    max_length = 2
        # 6. num = 2
        #    left_length = 1 (num_to_sequence_length[1]), right_length = 1 (num_to_sequence_length[3]), current_length = 4
        #    num_to_sequence_length = {100: 1, 4: 4, 200: 1, 1: 4, 3: 4, 2: 4}
        #    max_length = 4
        # The longest consecutive sequence is [1, 2, 3, 4], so the function returns 4.

# Time complexity: O(N)
# Space complexity: O(N)
def longest_consecutive_sequence(nums):
    numSet  = set(nums)
    longest = 0
    for num in numSet :
        if (num - 1) not in numSet:
            length  = 1
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest 