# Time complexity: O(V⋅E)
def bellman_ford(vertex, start, n):
    """
    Trova il cammino minimo da un nodo sorgente a tutti gli altri nodi in un grafo.
    
    :param vertex: Lista di archi rappresentata come [(u, v, w)], dove u è il nodo sorgente,
                   v è il nodo destinazione, e w è il peso dell'arco.
    :param start: Nodo di partenza.
    :param n: Numero totale di nodi nel grafo.
    :return: Lista delle distanze minime o None se è presente un ciclo di peso negativo.
    """
    distance = [float("inf")] * n
    distance[start] = 0

    # Ciclo principale dell'algoritmo
    for _ in range(n - 1):
        updated = False
        for u, v, w in vertex:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                updated = True
        # Termina prima se non ci sono stati aggiornamenti
        if not updated:
            break

    # Controllo per cicli di peso negativo
    for u, v, w in vertex:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            return None  # Rilevato ciclo negativo

    return distance

def bellman_ford_matrix(graph, start):
    """
    Trova il cammino minimo da un nodo sorgente a tutti gli altri nodi in un grafo.
    
    :param graph: Matrice di adiacenza dove graph[u][v] rappresenta il peso dell'arco (u, v).
                  Usa float("inf") per archi non esistenti.
    :param start: Nodo di partenza.
    :return: Lista delle distanze minime o None se è presente un ciclo di peso negativo.
    """
    n = len(graph)
    distance = [float("inf")] * n
    distance[start] = 0

    # Ciclo principale dell'algoritmo
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            for v in range(n):
                if graph[u][v] != float("inf") and distance[u] != float("inf") and distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    updated = True
        # Termina prima se non ci sono stati aggiornamenti
        if not updated:
            break

    # Controllo per cicli di peso negativo
    for u in range(n):
        for v in range(n):
            if graph[u][v] != float("inf") and distance[u] != float("inf") and distance[u] + graph[u][v] < distance[v]:
                return None  # Rilevato ciclo negativo

    return distance

def bellman_ford_adj_list(graph, start):
    """
    Trova il cammino minimo da un nodo sorgente a tutti gli altri nodi in un grafo.

    :param graph: Lista di adiacenza, dove graph[u] è una lista di tuple (v, w),
                  con v nodo adiacente e w peso dell'arco (u, v).
    :param start: Nodo di partenza.
    :return: Lista delle distanze minime o None se è presente un ciclo di peso negativo.
    """
    n = len(graph)
    distance = [float("inf")] * n
    distance[start] = 0

    # Ciclo principale dell'algoritmo
    for _ in range(n - 1):
        updated = False
        for u in range(n):
            for v, w in graph[u]:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    updated = True
        # Termina prima se non ci sono stati aggiornamenti
        if not updated:
            break

    # Controllo per cicli di peso negativo
    for u in range(n):
        for v, w in graph[u]:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                return None  # Rilevato ciclo negativo

    return distance
