# Time complexity: O(n * m) where n = len(s1) and m = len(s2)
# Space complexity: O(n * m)
def is_interleaving(s1, s2, target):
    # Controllo preliminare: la lunghezza di s1 + s2 deve corrispondere a target
    if len(s1) + len(s2) != len(target):
        return False

    # Lunghezze di s1 e s2
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Dizionario per memoization
    memo = {}

    # Funzione ricorsiva per verificare l'interleaving
    def check_interleaving(index_s1, index_s2):
        # Caso base: abbiamo usato tutti i caratteri di s1 e s2
        if index_s1 == len_s1 and index_s2 == len_s2:
            return True

        # Controlliamo se il risultato per questo stato è già memorizzato
        if (index_s1, index_s2) in memo:
            return memo[(index_s1, index_s2)]

        # Risultato inizialmente falso
        result = False

        # Verifica se il carattere di s1 corrisponde a quello corrente di target
        if index_s1 < len_s1 and s1[index_s1] == target[index_s1 + index_s2]:
            result = result or check_interleaving(index_s1 + 1, index_s2)

        # Verifica se il carattere di s2 corrisponde a quello corrente di target
        if index_s2 < len_s2 and s2[index_s2] == target[index_s1 + index_s2]:
            result = result or check_interleaving(index_s1, index_s2 + 1)

        # Salviamo il risultato in memo
        memo[(index_s1, index_s2)] = result
        return result

    # Avvio del controllo dall'inizio delle stringhe
    return check_interleaving(0, 0)

# dp[0][0] = True, perché due stringhe vuote interleavano una terza stringa vuota
def is_interleaving_dp(s1, s2, s3):
    # Controllo preliminare: le lunghezze di s1 e s2 devono sommare quella di s3
    if len(s1) + len(s2) != len(s3):
        return False

    len_s1, len_s2 = len(s1), len(s2)

    # Inizializziamo una matrice (len_s1 + 1) x (len_s2 + 1) con valori False
    dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Iteriamo per riempire la tabella
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            # Caso base: entrambe le stringhe vuote
            if i == 0 and j == 0:
                dp[i][j] = True
            # Se stiamo usando caratteri solo da s1
            elif i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            # Se stiamo usando caratteri solo da s2
            elif j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]

    # Restituiamo il valore finale
    return dp[len_s1][len_s2]