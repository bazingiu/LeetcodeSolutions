# Time complexity: O(m * n)
# Space complexity: O(m * n)
def calcola_distanza_edit(parola1, parola2):
    # Dizionario per memorizzare i risultati intermedi
    memo = {}
    
    def calcola(i, j):
        # Se la distanza tra le due sottostringhe è già stata calcolata, ritorna il risultato
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Caso base: se una delle due parole è vuota
        if i == 0:
            return j
        if j == 0:
            return i
        
        # Se i caratteri sono uguali, non è necessaria alcuna operazione
        if parola1[i - 1] == parola2[j - 1]:
            risultato = calcola(i - 1, j - 1)
        else:
            # Altrimenti prendi il minimo tra le tre operazioni
            risultato = 1 + min(
                calcola(i - 1, j),     # Cancellazione
                calcola(i, j - 1),     # Inserimento
                calcola(i - 1, j - 1)  # Sostituzione
            )
        
        # Memorizza il risultato prima di restituirlo
        memo[(i, j)] = risultato
        return risultato
    
    # Chiamata iniziale per calcolare la distanza tra le parole intere
    return calcola(len(parola1), len(parola2))

"""
    a b c
 |0|1|2|3 
a|1|0|1|2 
b|2|1|0|1
d|3|2|1|1

matrice[i - 1][j] # Cancellazione
matrice[i][j - 1],     # Inserimento
atrice[i - 1][j - 1]) # Sostituzione
"""

def calcola_distanza_edit(parola1, parola2):
    # Ottieni la lunghezza delle parole
    len_parola1, len_parola2 = len(parola1), len(parola2)
    
    # Crea una matrice 2D per memorizzare i risultati dei sottoproblemi
    matrice = [[0] * (len_parola2 + 1) for _ in range(len_parola1 + 1)]
    
    # Riempi la matrice
    for i in range(len_parola1 + 1):
        for j in range(len_parola2 + 1):
            # Se una delle due parole è vuota, la distanza è la lunghezza dell'altra parola
            if i == 0:
                matrice[i][j] = j
            elif j == 0:
                matrice[i][j] = i
            elif parola1[i - 1] == parola2[j - 1]:
                # Se i caratteri sono uguali, non è necessario nessun cambiamento
                matrice[i][j] = matrice[i - 1][j - 1]
            else:
                # Altrimenti, prendi il minimo tra le tre operazioni (inserimento, cancellazione, sostituzione)
                matrice[i][j] = 1 + min(matrice[i - 1][j],     # Cancellazione
                                        matrice[i][j - 1],     # Inserimento
                                        matrice[i - 1][j - 1]) # Sostituzione
    
    # La risposta finale si trova nell'angolo in basso a destra della matrice
    return matrice[len_parola1][len_parola2]
