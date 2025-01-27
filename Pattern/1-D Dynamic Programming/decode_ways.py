# Recursive
def decode_ways(s):
    n = len(s)
    results = []

    # Mappa i numeri da 1 a 26 alle lettere dell'alfabeto
    number_to_letter = {str(i): chr(64 + i) for i in range(1, 27)}

    def decode(index, partial_result):
        # Caso base: abbiamo raggiunto la fine della stringa
        if index == n:
            results.append(''.join(partial_result))
            return

        # Decodifica un singolo numero
        if s[index] in number_to_letter:
            decode(index + 1, partial_result + [number_to_letter[s[index]]])

        # Decodifica due numeri consecutivi (se valido)
        if index + 1 < n and s[index:index + 2] in number_to_letter:
            decode(index + 2, partial_result + [number_to_letter[s[index:index + 2]]])

    # Avvia la decodifica
    decode(0, [])
    return results

# Iterative 
def decode_ways(s):
    n = len(s)
    
    # Caso base: stringa vuota
    if n == 0:
        return 0
    
    # dp[i] rappresenta il numero di modi per decodificare s[:i]
    dp = [0] * (n + 1)
    dp[0] = 1  # 1 modo per decodificare la stringa vuota
    
    # Il primo carattere è valido?
    dp[1] = 1 if s[0] != '0' else 0
    
    for i in range(2, n + 1):
        # Singolo carattere valido
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Due caratteri validi
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]
