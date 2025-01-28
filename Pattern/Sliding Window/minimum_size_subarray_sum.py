# Time complexity: O(N) each elements is visited max two times
# Space complexity: O(1)
def minimum_size_subaarray_sum(target, nums):
    left = 0
    current_sum = 0
    min_size = float("inf")
    
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_size = min(min_size, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_size if min_size != float("inf") else 0

            