import heapq

def network_delay_time(n, times, start_node):
    # Inizializza la distanza a infinito per ogni nodo
    distances = [float('inf')] * (n + 1)
    # Costruisci la lista di adiacenza per rappresentare il grafo
    adjacency_list = {i: [] for i in range(1, n + 1)}

    for source, target, travel_time in times:
        adjacency_list[source].append((travel_time, target))

    # La distanza al nodo di partenza è 0
    distances[start_node] = 0
    # Usa una coda di priorità per tenere traccia del prossimo nodo da visitare
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)

        # Se la distanza attuale è già maggiore di quella registrata, salta il nodo
        if current_time > distances[current_node]:
            continue

        # Esplora i nodi vicini
        for travel_time, neighbor in adjacency_list[current_node]:
            new_time = current_time + travel_time
            # Se si trova una distanza più breve, aggiornala e aggiungi il vicino alla coda
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, neighbor))

    # Controlla se ci sono nodi non raggiungibili
    for i in range(1, n + 1):
        if distances[i] == float('inf'):
            return -1

    # Ottieni il tempo massimo per raggiungere tutti i nodi
    max_time = max(distances[1:])  # Escludi l'indice 0, poiché non corrisponde a nessun nodo
    return max_time

# Time complexity = O (E log V)
# poiche ci sono al massimo E aggiornamenti e V estrazioni
# Space complexity = O (V + E)