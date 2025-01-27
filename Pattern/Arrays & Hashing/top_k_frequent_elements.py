from collections import Counter
import heapq

# soluzione con heap
# time complexity: O(N * logK) dove N è il numero di elementi e K è il numero di elementi da restituire
# spaziale: O(N) per memorizzare la frequenza degli elementi

def top_K_frequent_elements(nums, k):
    # Conta la frequenza di ciascun elemento
    # O(N)
    element_freq = Counter(nums)
    
    # Utilizza una min-heap per mantenere i k elementi più frequenti
    heap = []
    #O(N * logK)
    for num, freq in element_freq.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Estrae gli elementi dalla heap
    top_k_elements = [heapq.heappop(heap)[1] for _ in range(len(heap))]
    top_k_elements.reverse()  # Opzionale: per avere gli elementi in ordine decrescente di frequenza
    
    return top_k_elements

# soluzione con bucket sort
# time complexity: O(N) dove N è il numero di elementi
# spaziale: O(N) per memorizzare la frequenza degli elementi
def top_K_frequent_elements(nums, k):
    # Conta la frequenza di ciascun elemento - O(N)
    element_freq = Counter(nums)
    
    # Trova la frequenza massima - O(N)
    max_freq = max(element_freq.values())
    
    # Crea i bucket fino alla frequenza massima - O(max_freq)
    buckets = [[] for _ in range(max_freq + 1)]
    for num, freq in element_freq.items():
        buckets[freq].append(num)
    
    # Itera sui bucket in ordine decrescente per trovare i top k - O(N)
    top_k_elements = []
    for i in range(max_freq, 0, -1):  # Partendo dalla frequenza massima
        top_k_elements.extend(buckets[i])
        if len(top_k_elements) >= k:
            break
    
    return top_k_elements[:k]
