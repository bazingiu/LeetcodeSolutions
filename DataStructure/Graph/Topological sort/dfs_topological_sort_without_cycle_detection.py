# O(V +E)
def topological_sort(graph):
    """
    Esegue l'ordinamento topologico su un grafo diretto aciclico (DAG).
    
    Args:
        graph (dict): Dizionario rappresentante il grafo {nodo: [vicini]}.

    Returns:
        list: Lista dei nodi in ordine topologico.
    """
    visited_nodes = set()  # Traccia i nodi visitati
    topological_order = []  # Lista per memorizzare l'ordine topologico

    def dfs(node):
        """
        Visita in profondità il grafo partendo da un nodo.
        
        Args:
            node (str): Nodo corrente.
        """
        if node not in visited_nodes:
            visited_nodes.add(node)  # Segna il nodo come visitato
            for neighbor in graph[node]:  # Esplora i nodi vicini
                dfs(neighbor)
            topological_order.append(node)  # Aggiungi il nodo in ordine topologico

    # Avvia la DFS per ogni nodo non ancora visitato
    for current_node in graph:
        dfs(current_node)

    # Restituisce l'ordine topologico (inverte la lista per ottenere l'ordine corretto)
    return topological_order[::-1]