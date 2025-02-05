def print_spiral_matrix(n):
    # Creazione della matrice vuota
    matrix = [[0] * n for _ in range(n)]
    
    num = 1  # Numero iniziale
    top, bottom, left, right = 0, n - 1, 0, n - 1

    # Riempire la matrice in senso orario
    while top <= bottom and left <= right:
        # Riga superiore
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Colonna destra
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Riga inferiore
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Colonna sinistra
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    # Stampa della matrice
    for row in matrix:
        print(' '.join(map(str, row)))

# Esempio di utilizzo
n = 4  # Cambia il valore di n per diverse dimensioni della matrice
print_spiral_matrix(n)
