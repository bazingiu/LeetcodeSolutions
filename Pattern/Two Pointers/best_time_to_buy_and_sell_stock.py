# Time complexity: O(N)
# Space complexity: O(1)
def best_time_to_buy_and_sell_stock(prices):
    if not prices or len(prices) < 2:
        return -1  # Not enough data to calculate profit
    
    buy = prices[0]  # Set the initial buying price to the first price in the list
    revenue = 0  # Initialize the revenue (profit) to 0

    for price in prices[1:]:
        # Update the minimum buying price if a lower price is found
        if price < buy:
            buy = price
        else:
            # Calculate the profit and update the maximum profit (revenue)
            revenue = max(revenue, price - buy)

    return revenue
