class Solution:
    """
    Checks if there are any duplicate elements in the list 'nums'.
    Args:
        nums (List[int]): The list of integers to check for duplicates.
    Returns:
        bool: True if there are duplicates, False otherwise.

    Time Complexity: O(n), where n is the number of elements in the list.
    Space Complexity: O(n), where n is the number of elements in the list.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for number in nums:
            if number in seen_numbers:
                return True
            seen_numbers.add(number)
        return False