# Complessità:
# La complessità temporale di questa funzione è O(n!), dove n è la lunghezza dell'array.
# Questo perché ci sono n! permutazioni possibili di un array di lunghezza n.
# La complessità spaziale è O(n) per l'uso dello stack di chiamate nella ricorsione,
# più O(n!) per memorizzare tutte le permutazioni.

def generate_permutations(arr):
    result = []

    def backtrack(start_index):
        # Caso base: se l'indice di partenza è uguale alla lunghezza dell'array,
        # significa che abbiamo una permutazione completa, quindi la aggiungiamo al risultato.
        if start_index == len(arr):
            result.append(arr[:])
        else:
            # Passo ricorsivo: scambiamo ogni elemento a partire dall'indice di partenza
            # con l'elemento corrente e chiamiamo ricorsivamente la funzione per il prossimo indice.
            for i in range(start_index, len(arr)):
                arr[start_index], arr[i] = arr[i], arr[start_index]
                backtrack(start_index + 1)
                arr[start_index], arr[i] = arr[i], arr[start_index]

    backtrack(0)
    return result

array = [1, 4, 3]
print(generate_permutations(array))

# Esempio di utilizzo:
# Dato l'array [1, 4, 3], la funzione permute restituirà tutte le permutazioni possibili:
# [[1, 4, 3], [1, 3, 4], [4, 1, 3], [4, 3, 1], [3, 4, 1], [3, 1, 4]]
# Passo 1 (start = 0):
#   - Scambia 1 con 1 (indice 0): [1, 4, 3]
#     Passo 2 (start = 1):
#       - Scambia 4 con 4 (indice 1): [1, 4, 3]
#         Passo 3 (start = 2):
#           - Aggiungi la permutazione [1, 4, 3]
#       - Scambia 4 con 3 (indice 2): [1, 3, 4]
#         Passo 3 (start = 2):
#           - Aggiungi la permutazione [1, 3, 4]
#     ...
