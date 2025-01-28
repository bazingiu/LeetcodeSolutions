# Space complexity: O(N)
def find_all_missing_numbers(nums):
    n = len(nums)
    set_nums = set(nums) # O(N)
    all_nums = set(range(1, n + 1)) # O(N)
    missing = all_nums - set_nums #O(n) - set difference we get missing numbers
    return list(missing)

# Space complexity: O(N)
def find_all_missing_numbers(nums):
    set_nums = set(nums) # O(N)
    missing = []
    for num in range(1, len(nums) + 1): # O(N)
        if num not in set_nums:
            missing.add(num)  # (Errore: append va usato qui)
    return missing
