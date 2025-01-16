# Problem: Generate all possible subsets of a list of integers.

# Approach: Backtracking
def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    current_subset = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(current_subset[:])
            return
        current_subset.append(nums[start])
        backtrack(start + 1)
        current_subset.pop()
        backtrack(start + 1)
    
    backtrack(0)
    return result

# Time complexity: O(2^n)
# Space complexity: O(n)

# Approach: Iterative 
def generate_subsets(self, nums):
    """
    Generate all possible subsets of a list of integers.

    :param nums: List of integers to generate subsets from.
    :return: A list of lists, where each list is a subset of the input list.

    Time Complexity: O(2^n * n), where n is the length of the input list. 
    This is because there are 2^n possible subsets and each subset takes O(n) time to create.
    Space Complexity: O(2^n * n) to store all the subsets.
    """
    result = [[]]  # Inizia con il sottoinsieme vuoto
    for num in nums:
        result += [subset + [num] for subset in result]  # Aggiungi num a ogni sottoinsieme esistente
    return result