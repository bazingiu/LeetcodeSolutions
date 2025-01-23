def find_subsets_with_duplicates(nums):
    """
    Finds all possible subsets of a list of numbers, including handling duplicates.
    Args:
        nums (List[int]): A list of integers that may contain duplicates.
    Returns:
        List[List[int]]: A list of lists, where each list is a unique subset of the input list.
    """
    nums.sort()
    subsets = []
    
    def backtrack(start_index, current_subset):
        subsets.append(current_subset[:])
        
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    
    backtrack(0, [])
    return subsets
