def course_schedule_two(prerequisites, numCourses):
    graph = {i : [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Stati dei nodi: 0 = non visitato, 1 = in visita, 2 = completamente visitato
    states = [0] * numCourses
    result = []
    def topological__sort(node):
        if states[node] == 1:  # Nodo già in visita → ciclo trovato
            return False
        
        if states[node] == 2:  # Nodo già completamente visitato → nessun ciclo
            return True
        
        states[node] = 1
        for neighbor in graph[node]:
            if not topological__sort(neighbor): # Se un ciclo viene trovato, interrompi
                return False
        
        states[node] = 2
        result.append(node)
        return True
    
    for course in graph.keys(): 
        if states[course] == 0:
            if not topological__sort(course):
                return []
    
    return result[::-1] 
    
# Time complexity: O(V + E)
# Space complexity: O(V + E)