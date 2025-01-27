def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for current_amount in range(1, amount + 1):
        for coin in coins: 
            if current_amount - coin >= 0:  # Se il valore è raggiungibile
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
    
    # Se il valore finale è ancora "infinito", significa che non possiamo ottenere quel `amount`.
    return dp[amount] if dp[amount] != float('inf') else -1

# Complessità temporale O(amount * number_of_coin)
# complessita spaziale O(amount)