# Space complexity: O(N)
def find_all_missing_numbers(nums):
    n = len(nums)
    set_nums = set(nums) # O(N)
    all_nums = set(range(1, n + 1)) # O(N)
    missing = all_nums - set_nums #O(n) - set difference we get missing numbers
    return list(missing)
