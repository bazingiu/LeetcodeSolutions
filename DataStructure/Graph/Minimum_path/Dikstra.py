import heapq
# Trovare il cammino minimo tra un nodo e tutti gli altri nodi in un grafo direzionato con pesi positivi O((V+E)logV)
def dijkstra(graph, start):
    # Inizializza tutte le distanze a infinito e la distanza di partenza a zero
    distance = {node: float("inf") for node in graph}
    distance[start] = 0
    
    # Coda di priorità per i nodi da esplorare
    priority_queue = [(0, start)]  # distanza, nodo
    visited = set()
    
    while priority_queue:
        # Estrai il nodo con la distanza minima
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Se la distanza corrente è maggiore di quella registrata, salta il nodo
        if current_node in visited:
            continue
        
        visited.add(current_node)
        # Esplora i vicini
        for neighbor, weight in graph[current_node]:
            distance_to_neighbor = current_distance + weight
            
            # Aggiorna la distanza se è minore di quella registrata
            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
    
    return distance