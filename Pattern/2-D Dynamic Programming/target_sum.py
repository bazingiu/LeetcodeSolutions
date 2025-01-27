# Time complexity: O(n * t) n = number of elements and t range of possible amount
# Space complexity: O(n * t)
def target_sum(nums, target):
    # Memoization dictionary to store intermediate results
    memo = {}

    # Helper function to calculate the number of ways
    def sum_to_target(amount, index):
        # Base case: if we've processed all numbers
        if index == len(nums):
            # Check if the remaining amount is zero
            return 1 if amount == 0 else 0
        
        # Check if the subproblem has already been solved
        if (amount, index) in memo:
            return memo[(amount, index)]
        
        # Recursive cases: try adding or subtracting the current number
        add = sum_to_target(amount - nums[index], index + 1)
        subtract = sum_to_target(amount + nums[index], index + 1)
        
        # Memoize the result
        memo[(amount, index)] = add + subtract
        return memo[(amount, index)]
    
    # Start the recursion with the full target and the first index
    return sum_to_target(target, 0)

# Bottom up solution
def target_sum(nums, target):