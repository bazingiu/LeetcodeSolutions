# ------ Creazione di una deque ------ #
from collections import deque
deq = deque()  # Inizializza una deque vuota.
deq_copy = deque(deq)  # Crea una copia di deq
print(2 in deq)  # Output: False
deq = deque(list(deq)[:3])  # Limita a 3 elementi.

# ------ Metodi principali per manipolare una deque ------ #
# append(value): Aggiunge un elemento alla fine della deque.
deq.append('a')  # Risultato: deque(['a'])

# appendleft(value): Aggiunge un elemento all'inizio della deque.
deq.appendleft(2)  # Risultato: deque([2, 'a'])

# pop(): Rimuove e restituisce l'ultimo elemento della deque.
deq.pop()  # Rimuove l'ultimo elemento. Risultato: deque([2])

# popleft(): Rimuove e restituisce il primo elemento della deque.
deq.popleft()  # Rimuove il primo elemento. Risultato: deque([])

# ------ Altri metodi utili ------ #
# extend(iterable): Aggiunge gli elementi di un iterabile alla fine della deque.
deq.extend([3, 4, 5])  # Risultato: deque([3, 4, 5])

# extendleft(iterable): Aggiunge gli elementi di un iterabile all'inizio della deque (in ordine inverso).
deq.extendleft([6, 7])  # Risultato: deque([7, 6, 3, 4, 5])

# rotate(n): Ruota la deque di n posizioni (a destra se n è positivo, a sinistra se negativo).
deq.rotate(1)  # Ruota di 1 posizione. Risultato: deque([5, 7, 6, 3, 4])

# clear(): Rimuove tutti gli elementi della deque.
deq.clear()  # Risultato: deque([])

# ------ Accesso diretto agli elementi ------ #
# Le deque supportano l'accesso diretto per indice (come le liste).
deq.extend([10, 20, 30])  # Aggiunge elementi per test.
print(deq[0])  # Stampa il primo elemento. Output: 10
print(deq[-1])  # Stampa l'ultimo elemento. Output: 30

# ------ Creazione con dimensione massima ------ #
# Puoi definire una dimensione massima usando il parametro maxlen.
deq = deque(maxlen=3)  # La deque può contenere massimo 3 elementi.
deq.extend([1, 2, 3])  # Risultato: deque([1, 2, 3], maxlen=3)
deq.append(4)  # Rimuove il primo elemento e aggiunge 4. Risultato: deque([2, 3, 4], maxlen=3)

# ------ Altre note ------ #
# Vantaggi:
# - Le deque sono più efficienti delle liste per aggiunte e rimozioni agli estremi (O(1)).
# - Ideali per code e stack.

# Limiti:
# - Non ottimizzate per ricerca o accesso casuale (come le liste).

# Esempio di deque con maxlen:
print(deq)  # Output: deque([2, 3, 4], maxlen=3)
