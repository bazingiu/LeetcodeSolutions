"""
      a c e
    a 3|2|1|0
    b 2|2|1|0
    c 2|2|1|0
    d 1|1|1|0
    e 1|1|1|0
      0|0|0|0
      
Base Cases:
    If either string is empty (i = len(s1) or j = len(s2)), the LCS is 0.
Recursive Formula:
When Characters Match (s1[i] == s2[j]):
    LCS[i][j] = 1 + LCS[i+1][j+1]
    we go orizontaly in the bottom up approach
When Characters Do Not Match (s1[i] != s2[j]):
    LCS[i][j] = max( LCS[i+1][j],LCS[i][j+1])
    we go down and right in the bottom up approach
"""

# Time complexity: O(m * n)
# Space complexity: O(m * n)
def longest_common_subsequence(text1, text2):
    substring_len = len(text2)
    string_len = len(text1)
    # Initialize a 2D matrix with zeros
    matrix = [[0] * (substring_len + 1) for _ in range(string_len + 1)]
    
    # Fill the matrix bottom-up
    for i in range(string_len - 1, -1, -1):
        for j in range(substring_len - 1, -1, -1):
            if text1[i] == text2[j]:
                # Characters match, add 1 to the diagonal value
                matrix[i][j] = 1 + matrix[i + 1][j + 1]
            else:
                # Characters do not match, take the maximum of right and down
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])
    
    return matrix[0][0]  # The LCS length is in the top-left cell

# Time complexity:  O(m⋅n)	
# Space complexity: O(n)
# I is the position in text1 and j the position in text2
def longest_common_subsequence(text1, text2):
    substring_len = len(text2)
    string_len = len(text1)

    # Utilizzo di due righe per memorizzare i valori intermedi
    previous = [0] * (substring_len + 1)
    current = [0] * (substring_len + 1)

    for i in range(string_len - 1, -1, -1): # Da basso verso l'alto
        for j in range(substring_len - 1, -1, -1): # Da destra verso sinistra
            if text1[i] == text2[j]: # Caratteri uguali
                current[j] = 1 + previous[j + 1] #diagonale in basso a destra
            else: # Caratteri diversi
                current[j] = max(previous[j], current[j + 1]) # valore in basso e valore a destra
        # Aggiorna `previous` con `current` per il prossimo ciclo
        previous = current[:]

    return previous[0]