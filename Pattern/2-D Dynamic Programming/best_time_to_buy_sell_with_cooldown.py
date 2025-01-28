"""
At each day i, you can decide to either:
Buy -> i + 1
Sell -> i+2 
Skip: Do nothing and move to the next day i+1.

we can use cache for (i, buy/sell) (n possible value, 2 different state) so n * 2
"""

def best_time_to_buy_sell_with_cooldown(prices):
    # Memoization table to store the results of subproblems
    memo = {}

    # Recursive helper function
    def best(i, holding):
        # Base case: if we're out of days, no profit can be made
        if i >= len(prices):
            return 0
        
        # Check if the result for this state is already computed
        if (i, holding) in memo:
            return memo[(i, holding)]
        
        # If holding is 0, we can buy or skip
        if holding == 0:
            profit = max(
                - prices[i] + best(i + 1, 1),  # Buy the stock and go to holding state
                best(i + 1, 0)                # Skip this day
            )
        else:
            # If holding is 1, we can sell or skip
            profit = max(
                prices[i] + best(i + 2, 0),  # Sell the stock and go to cooldown state
                best(i + 1, 1)               # Skip this day
            )
        
        # Store the result in the memoization table
        memo[(i, holding)] = profit
        return profit

    # Start from day 0, with no stock in hand
    return best(0, 0)
            
            
    