def topological_sort_with_cycle_detection(graph):
    visited_nodes = set()      # Nodi già visitati
    recursion_stack = set()    # Nodi nella pila di ricorsione
    topological_order = []     # Risultato dell'ordinamento topologico
    has_cycle = [False]        # Flag per rilevare cicli

    def dfs(node):
        if has_cycle[0]:  # Se abbiamo già trovato un ciclo, termina
            return
        if node not in visited_nodes:
            visited_nodes.add(node)
            recursion_stack.add(node)  # Aggiungi il nodo alla pila di ricorsione

            for neighbor in graph[node]:
                if neighbor not in visited_nodes:
                    dfs(neighbor)
                elif neighbor in recursion_stack:
                    # Se il vicino è nella pila di ricorsione, abbiamo un ciclo
                    has_cycle[0] = True
                    return

            recursion_stack.remove(node)  # Rimuovi il nodo dalla pila di ricorsione
            topological_order.append(node)

    for current_node in graph:
        if current_node not in visited_nodes:
            dfs(current_node)
            if has_cycle[0]:  # Interrompi se è stato rilevato un ciclo
                break

    if has_cycle[0]:
        raise ValueError("Il grafo contiene un ciclo e non può essere ordinato topologicamente.")
    
    return topological_order[::-1]  # Ordine corretto

# Test con un grafo senza cicli
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['E'],
    'E': ['F'],
    'F': ['D']  # Questo crea un ciclo
}

try:
    order = topological_sort_with_cycle_detection(graph)
    print("Ordine topologico:", order)
except ValueError as e:
    print(e)
