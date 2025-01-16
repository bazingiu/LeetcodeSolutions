def maxProfit(self, prices):
    """
    Calculate the maximum profit that can be achieved from buying and selling stock.

    :param prices: List[int] - A list of stock prices where prices[i] is the price of a given stock on the ith day.
    :return: int - The maximum profit that can be achieved. If no profit is possible, returns 0.

    Time complexity: O(n), where n is the length of the list of prices.
    Space complexity: O(1), as it uses only a constant number of additional variables.
    """
    min_price = float('inf')  # Initialize the minimum price to a very large value
    max_profit = 0  # Initialize the maximum profit to 0

    # Iterate through prices to find the minimum price and calculate the maximum profit
    for price in prices:
        if price < min_price:  # Update the minimum price if a lower price is found
            min_price = price
        elif price - min_price > max_profit:  # Update max profit if the current profit is greater
            max_profit = price - min_price
    
    return max_profit  # Return the maximum profit found
