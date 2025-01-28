from collections import deque, defaultdict

# Time complexity: O(V + E)
def kahn_algorithm(graph):
    # Step 1: Calculate in-degree of each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Step 2: Initialize queue with nodes having in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    
    # Step 3: Perform topological sort
    topo_order = []
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        
        # Reduce the in-degree of neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check if topological sort is successful
    if len(topo_order) == len(graph):
        return topo_order
    else:
        # The graph has a cycle
        return None