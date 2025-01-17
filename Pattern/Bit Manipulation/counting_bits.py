def countBits(n):
    """
    Given a non-negative integer n, this function returns an array representing 
    the number of 1's in the binary representation of each number from 0 to n.
    :param n: A non-negative integer.
    :return: A list of integers where the ith element is the number of 1's in 
             the binary representation of i.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """      
    dp = [0] * (n + 1)
    # Offset to track the most significant bit
    offset = 1

    # Iterate through each number from 1 to n
    for i in range(1, n + 1):
        # Update the offset when it reaches the next power of two
        if offset * 2 == i:
            offset = i
        # Calculate the number of 1's by adding 1 to the number of 1's in the number i - offset
        dp[i] = 1 + dp[i - offset]
    
    return dp

# Example:
# For n = 5, the binary representations are:
# 0 -> 0 (0)
# 1 -> 1 (1)
# 2 -> 10 (1)
# 3 -> 11 (2)
# 4 -> 100 (1)
# 5 -> 101 (2)
# So, the function will return [0, 1, 1, 2, 1, 2]