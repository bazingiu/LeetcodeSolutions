def minCostClimbingStairs(self, cost):
    """
    Calculate the minimum cost to reach the top of a staircase where each step has a cost associated with it.

    :type cost: List[int] - A list where cost[i] is the cost of stepping on the ith step.
    :rtype: int - The minimum cost to reach the top of the staircase.
    
    Time complexity: O(n) - We iterate through the cost array once.
    Space complexity: O(n) - We use an additional array of size n+1.
    """
    n = len(cost)
    min_cost = [0] * (n + 1)
    
    for i in range(2, n + 1):
        min_cost[i] = min(cost[i - 1] + min_cost[i - 1], 
                          cost[i - 2] + min_cost[i - 2])
    
    return min_cost[n]

    # Base cases:
    # min_cost[0] = 0 (no cost to start at the ground)
    # min_cost[1] = 0 (no cost to step on the first step)
    
    # Recursive step:
    # To reach step i, we can:
    # 1. Step from i-1 with cost[i-1] + min_cost[i-1]
    # 2. Step from i-2 with cost[i-2] + min_cost[i-2]
    # Take the minimum of these two options