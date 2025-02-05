def topological_sort_with_cycle_detection(graph):
    visited_nodes = set()    # Insieme dei nodi già visitati
    recursion_stack = []     # Pila per rilevare cicli
    topological_order = []   # Lista dell'ordinamento topologico

    def dfs(node):
        if node in recursion_stack:  # Se il nodo è nella pila di ricorsione, c'è un ciclo
            raise ValueError("Il grafo contiene un ciclo e non può essere ordinato topologicamente.")

        if node in visited_nodes:  # Se il nodo è già visitato, termina
            return

        visited_nodes.add(node)
        recursion_stack.append(node)  # Aggiungi il nodo alla pila di ricorsione

        for neighbor in graph.get(node, []):  # Usa get() per gestire nodi senza adiacenze
            dfs(neighbor)

        recursion_stack.pop()  # Rimuovi il nodo dalla pila di ricorsione
        topological_order.append(node)

    for current_node in graph:
        if current_node not in visited_nodes:
            try:
                dfs(current_node)
            except ValueError as e:
                raise e  # Se troviamo un ciclo, fermiamo tutto immediatamente

    return topological_order[::-1]  # Restituiamo l'ordine corretto

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


def topological_sort_with_cycle_detection(graph):
    visited_nodes = set()    # Nodi già visitati
    recursion_stack = set()  # Pila per rilevare cicli
    topological_order = []   # Risultato dell'ordinamento topologico
    has_cycle = [False]      # Flag per rilevare cicli (lista mutabile)

    def dfs(node):
        if has_cycle[0]:  # Se abbiamo già trovato un ciclo, termina
            return
        
        if node in recursion_stack:  # Se il nodo è nella pila di ricorsione, c'è un ciclo
            has_cycle[0] = True
            return

        if node in visited_nodes:  # Se il nodo è già visitato, termina
            return

        visited_nodes.add(node)
        recursion_stack.add(node)  # Aggiungi il nodo alla pila di ricorsione

        for neighbor in graph.get(node, []):  # Usa get() per evitare errori su nodi senza adiacenze
            dfs(neighbor)

        recursion_stack.remove(node)  # Rimuovi il nodo dalla pila di ricorsione
        topological_order.append(node)

    for current_node in graph:
        if current_node not in visited_nodes:
            dfs(current_node)
            if has_cycle[0]:  # Interrompi se è stato rilevato un ciclo
                return None  # Indica che il grafo non è DAG e non può essere ordinato

    return topological_order[::-1]  # Ordine corretto
