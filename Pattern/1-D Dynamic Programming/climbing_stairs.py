def climbStairs(self, n):
    """
    Calculate the number of distinct ways to climb a staircase with `n` steps,
    where you can either climb 1 step or 2 steps at a time.
    
    :param n: The total number of steps in the staircase.
    :type n: int
    :return: The number of distinct ways to reach the top of the staircase.
    :rtype: int

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current_step, previous_step = 1, 1

    for _ in range(n - 1):
        current_step, previous_step = current_step + previous_step, current_step
    
    return current_step

    """    
    Example:
    Let's take n = 5 as an example.
    Initial state:
    current_step = 1, previous_step = 1

    Iteration 1:
    current_step = current_step + previous_step = 1 + 1 = 2
    previous_step = current_step (before update) = 1

    Iteration 2:
    current_step = current_step + previous_step = 2 + 1 = 3
    previous_step = current_step (before update) = 2

    Iteration 3:
    current_step = current_step + previous_step = 3 + 2 = 5
    previous_step = current_step (before update) = 3

    Iteration 4:
    current_step = current_step + previous_step = 5 + 3 = 8
    previous_step = current_step (before update) = 5

    Final result for n = 5:
    current_step = 8
    """
   