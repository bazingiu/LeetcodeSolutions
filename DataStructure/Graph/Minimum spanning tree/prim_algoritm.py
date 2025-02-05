import heapq

def prim_algorithm_with_predecessors(adjacency_list):
    """
    Args:
        adjacency_list (list of lists): Adjacency list representation of the graph where each element 
                                        is a list of tuples (neighbor, weight).

    Returns:
        tuple: (Total weight of the MST, List of edges in the MST)
               If the graph is not connected, returns (-1, []).
    """
    num_nodes = len(adjacency_list)
    visited = set()  # Track visited nodes
    min_heap = [(0, 0, -1)]  # (weight, node, parent), starting with node 0 and no parent (-1)
    total_weight = 0
    mst_edges = []  # List of edges forming the MST

    while min_heap:
        # Extract the edge with the smallest weight
        edge_weight, current_node, parent = heapq.heappop(min_heap)

        # Skip if the node is already included in the MST
        if current_node in visited:
            continue

        # Mark the node as visited
        visited.add(current_node)
        total_weight += edge_weight

        # If there is a valid parent, add it to the MST edges
        if parent != -1:
            mst_edges.append((parent, current_node, edge_weight))

        # Add all unvisited neighbors to the priority queue
        for neighbor, weight in adjacency_list[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, current_node))

    # Check if the MST includes all nodes (graph must be connected)
    if len(visited) == num_nodes:
        return total_weight, mst_edges
    else:
        return -1, []

# Example usage
graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

total_weight, mst_edges = prim_algorithm_with_predecessors(graph)
print("Total MST Weight:", total_weight)
print("MST Edges:", mst_edges)


# Time complexity: O((V+E)logV) 
# - Heap operation O(E log V)
# Space complexity: O(V+E)