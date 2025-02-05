# Graph as adj of directed graph 
def create_adj(vertex_list,  n):
    adj = {i : [] for i in range(n)}
    for u, v, w in vertex_list:
        adj[u].append([v,w])
        adj[v].append([u,w])


# Grafo con lettere
graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("D", 2)],
    "C": [("D", 1), ("E", 5)],
    "D": [("E", 3)],
    "E": []
}