"""
we dont wont same combination with different order
For any recursive call, only coins from the current index onward are considered.
This guarantees that combinations like [1, 2] and [2, 1] are counted as one combination because we never look backward in the list of coins.
"""
# Time complexity: O(c * amount)
def coin_change_two(coins, amount):
    # number of combination 
    memo = {}
    def make_amount(amount, index):
        # Base case: if amount is 0, there's one way to make it
        if amount == 0:
            return 1
        # Base case: if amount is negative, no valid combination exists
        if amount < 0:
            return 0
        
        if (amount, index) in memo:
            return memo[(amount, index)]
        
        num_of_ways = 0
        # Try using each coin starting from the current index
        for i in range(index, len(coins)):
            num_of_ways += make_amount(amount - coins[i], i)
        memo[(amount, index)] = num_of_ways
        
        return num_of_ways
            
"""
Bottom up solution 
  0 1 2 3 4 5
1|1|1|2|2|3|4|
2|1|0|1|0|1|1|
5|1|0|0|0|0|1|

Righe: Rappresentano gli importi da amount fino a 0
Colonne: Rappresentano le monete disponibili.
Celle: Indicano il numero di modi per ottenere l'importo corrispondente usando 
la moneta corrente e quelle sotto.

Per ogni cella, combiniamo:
A destra: I modi per ottenere l'importo usando la stessa moneta.
Sotto: I modi per ottenere l'importo usando solo le monete sotto.
ci muoviamo da destra a sinistra dall'ultima riga in su
È sufficiente memorizzare solo la riga corrente e la riga precedente, poiché ogni riga dipende solo dalla riga successiva.
"""
# Time complexity: O(number of coins * target_amount)
# Space complexity: O(target_amount)
def coin_change_two_bottom_up(coins, amount):
    previous = [0] * (amount + 1)
    current = [0] * (amount + 1)
    
    previous[0] = 1
    
    for coin in reversed(coins):
        for j in range(amount + 1): 
            # Calculate the number of ways using this coin (if possible)
            current[j] = previous[j]
            if j - coin >= 0:  # If we can use the current coin
                current[j] += current[j - coin]
        # Update the `previous` row for the next iteration
        previous = current[:]
    return previous[amount]