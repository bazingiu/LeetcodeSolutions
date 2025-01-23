def permute(nums):
    """
    Generate all possible permutations of a list of numbers.
    Args:
        nums (List[int]): A list of integers to permute.
    Returns:
        List[List[int]]: A list containing all permutations of the input list.
    Time Complexity: O(n * n!) where n is the length of the input list.
    Space Complexity: O(n! * n) for storing the permutations.
    """
    permutations = []
    
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[i], nums[start] = nums[start], nums[i]
    
    backtrack(0)
    return permutations

result = permute([1, 2, 3])
print(result)

"""
n! = number of permutations of a list of length n
each time a complete permutation is found, a copy of the list of length n is made which requires O(n)

Space complexity:
there are n! permutations and each is of length n, so the storage space is O(n! * n)
 """