from collections import defaultdict

# soluzione meno efficiente con ordinamento di ogni stringa
# O(N * L * logL) dove N è il numero di stringhe e L è la lunghezza della stringa
# spaziale: O(N * L) per memorizzare le stringhe
def group_anagrams(strs):
    anagram = defaultdict(list)
    for word in strs:
        sorted_s = ''.join(sorted(word))
        anagram[sorted_s].append(word)
    return anagram.values()

# soluzione più efficiente con conteggio delle lettere
# O(L) dove L è la lunghezza della stringa  per ogni stringa di cui conta i caratteri 
# questa operazione viene svolta N volte, dove n è il numero di stringhe
# quindi la complessità totale è O(N *L)
# spaziale: O(N * L) per memorizzare le stringhe
def group_anagrams(strs):
    anagram = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        anagram[tuple(count)].append(s)
    return anagram.values()