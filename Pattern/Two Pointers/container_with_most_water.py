def maxArea(self, heights: List[int]) -> int:
    """
    Calculate the maximum amount of water that can be contained by any two lines.

    Args:
        heights (List[int]): A list of integers representing the height of lines.

    Returns:
        int: The maximum amount of water that can be contained.

    Time Complexity: O(n), where n is the number of elements in the heights list.
    Space Complexity: O(1), as we are using a constant amount of extra space.
    """
    n = len(heights)
    left, right = 0, n - 1
    max_water = 0
    while left < right:
        left_height, right_height = heights[left], heights[right]
        max_water = max(max_water, min(left_height, right_height) * (right - left))
        if left_height < right_height:
            left += 1
        else:
            right -= 1
    return max_water