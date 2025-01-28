def tarjarian_algorithm(graph):
    index = 0 
    stack = []
    indices = {}
    lowlink = {}
    in_stack = set()
    sccs = []
    
    def dfs(node):
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        in_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in indices:
                dfs(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in in_stack:
                lowlink[node] = min(lowlink[node], indices[neighbor])
        
        if lowlink[node] == indices[node]:
            scc = []
            while True:
                w = stack.pop()
                in_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in indices:
            dfs(node)

    return sccs