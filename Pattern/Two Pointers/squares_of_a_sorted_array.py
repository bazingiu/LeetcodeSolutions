from collections import deque

# Time complexity: O(N)
# Space complexity: O(N) (the result has N elements)
def sorted_squares(nums):
    left, right = 0, len(nums) - 1
    result = deque()  # Usato per inserimenti efficienti in testa

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result.appendleft(left_square)
            left += 1
        else:
            result.appendleft(right_square)
            right -= 1

    return list(result)  # Converti il deque in lista prima di restituirlo
