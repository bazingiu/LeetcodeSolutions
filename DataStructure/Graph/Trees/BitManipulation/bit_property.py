# Numero di bit impostati in A = X
# Numero di bit impostati in B = Y
# Numero di bit impostati in A^B = Z

# Proprietà dell'operazione XOR (A^B):
# Proprietà 1: Z è pari se X + Y è pari -> X o Y è pari
# Proprietà 2: Z è dispari se X + Y è dispari -> X e Y sono dispari

# Esempio di bit impostati pari:
# A = 5, B = 3
# A = 101, B = 011
# A^B = 110 -> 2 bit impostati

# Esempio di bit impostati dispari:
# A = 7, B = 3
# A = 111, B = 011
# A^B = 100 -> 1 bit impostato

# Proprietà 3: Se A ha tutti i bit impostati e B ha tutti i bit impostati, allora A^B avrà nessun bit impostato.
# Proprietà 4: Se A ha nessun bit impostato e B ha nessun bit impostato, allora A^B avrà nessun bit impostato.
# Proprietà 5: Se A ha un solo bit impostato e B ha un solo bit impostato, allora A^B avrà nessun bit impostato se i bit sono nella stessa posizione, altrimenti avrà due bit impostati.
# Proprietà 6: Commutativa
# A ^ B == B ^ A

# Proprietà 7: Associativa
# (A ^ B) ^ C == A ^ (B ^ C)

# Proprietà 8: Identità
# A ^ 0 == A

# Proprietà 9: Auto-inversa
# A ^ A == 0

# Proprietà 10: Distribuzione rispetto all'AND
# (A & B) ^ (A & C) == A & (B ^ C)

# Proprietà 11: Distribuzione rispetto all'OR
# (A | B) ^ (A | C) == A | (B ^ C)

