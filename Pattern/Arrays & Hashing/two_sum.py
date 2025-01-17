def twoSum(self, numbers: List, target):
    """
    Given an array of integers `numbers` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    Args:
        numbers (List[int]): List of integers.
        target (int): The target sum.

    Returns:
        List[int]: Indices of the two numbers that add up to `target`. If no such pair exists, returns None.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    index_map = {}
    for index, number in enumerate(numbers): #O(n)
        complement = target - number   
        if complement in index_map: 
            return [index_map[complement], index] 
        index_map[number] = index
    return None