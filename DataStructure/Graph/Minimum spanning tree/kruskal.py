# Time complexity:
# O(E log E) for the sort of the edge 
# O(ElogE+Eα(N)) and an aproximization is O(E log E)
# Space complexity: O(N) for rank and parent + O(E) for the edge lists O(N + E)
def kruskal_mst(num_nodes, edge_list):
    """
    Trova il Minimum Spanning Tree (MST) di un grafo usando l'algoritmo di Kruskal.

    :param num_nodes: Numero di nodi nel grafo
    :param edge_list: Lista di archi (nodo1, nodo2, peso)
    :return: Lista di archi che formano il MST
    """
    # Ordina gli archi in ordine crescente di peso
    edge_list.sort(key=lambda edge: edge[2]) 

    # Inizializza la struttura Union-Find
    disjoint_set = UnionFind(num_nodes)

    # Lista per contenere gli archi del MST
    mst_edges = []

    for node1, node2, weight in edge_list:
        # Aggiungi l'arco se non forma un ciclo
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            disjoint_set.union(node1, node2)
            mst_edges.append((node1, node2, weight))

            # Fermati se abbiamo già n-1 archi
            if len(mst_edges) == num_nodes - 1:
                break

    return mst_edges
