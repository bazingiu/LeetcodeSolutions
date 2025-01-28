# Time Complexity: O(N)
# range(len(nums) + 1) O(N)
# sum(nums) O(N)
# Space complexity: O(1)

def missing_number(nums):
    return sum(range(len(nums) + 1) - sum(nums))

# Somma di numeri da 0 a n = n⋅(n+1) / 2
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

