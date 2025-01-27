# Time complexity: O(V^3)
# Space complexity: O(V*V)

def floyd_warshall(graph):
    """
    Finds the shortest paths between all pairs of nodes in a weighted graph.
    Works with negative weights but not with negative cycles.

    :param graph: A 2D list representing the adjacency matrix of the graph.
                  graph[i][j] is the weight of the edge from node i to node j,
                  or float('inf') if no such edge exists.
    :return: A 2D list where the value at [i][j] is the shortest distance from node i to node j.
    """
    num_vertices = len(graph)
    
    # Create a copy of the graph to store the shortest distances
    dist = [row[:] for row in graph]

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the shortest distance
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
graph = [
    [0, 3, 8, -4],
    [float('inf'), 0, float('inf'), 7],
    [float('inf'), 4, 0, float('inf')],
    [float('inf'), float('inf'), 6, 0]
]

# Print the shortest distance matrix
shortest_distances = floyd_warshall(graph)
for row in shortest_distances:
    print(row)