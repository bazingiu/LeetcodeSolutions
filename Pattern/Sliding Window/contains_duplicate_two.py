# Time complexity: O(N)
# Space complexity: O(k)
def contains_duplicate_two(nums, k): 
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i-k])
    return False