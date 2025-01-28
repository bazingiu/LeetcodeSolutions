from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Time complexity: O(V + E)
# Space complexity: O(V + E):
# - oldToNew -> O(V)
# - q -> O(V)
# - cloned graph -> O(V + E)
def cloneGraph(self, node):
    if not node:
        return None

    oldToNew = {}
    oldToNew[node] = Node(node.val) # creiamo il nuovo nodo
    q = deque([node])

    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in oldToNew:
                oldToNew[nei] = Node(nei.val) # lo creiamo e lo aggiungiamo alla coda 
                q.append(nei)
            oldToNew[cur].neighbors.append(oldToNew[nei]) # aggiungiamo la connessione 

    return oldToNew[node]