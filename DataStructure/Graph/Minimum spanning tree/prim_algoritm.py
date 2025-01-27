import heapq

def prim_algoritm(adjacency_list):
    """
    Args:
        adjacency_list (list of lists): Adjacency list representation of the graph where each element 
                                        is a list of tuples (neighbor, weight).

    Returns:
        int: The total weight of the MST, or -1 if the graph is not connected.
    """
    num_nodes = len(adjacency_list)
    visited = set()  # To keep track of visited nodes
    min_heap = [(0, 0)]  # Priority queue initialized with (weight, start_node)
    total_weight = 0

    while min_heap:
        # Extract the edge with the smallest weight
        edge_weight, current_node = heapq.heappop(min_heap)

        # Skip if the node is already included in the MST
        if current_node in visited:
            continue

        # Mark the node as visited and add the edge weight to the total cost
        visited.add(current_node)
        total_weight += edge_weight

        # Add all unvisited neighbors to the priority queue
        for neighbor, weight in adjacency_list[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))

    # Check if the MST includes all nodes (graph must be connected)
    return total_weight if len(visited) == num_nodes else -1

# Time complexity: O((V+E)logV) 
# - Heap operation O(E log V)
# Space complexity: O(V+E)