# Graph as adj of directed graph 
def create_adj(vertex_list,  n):
    adj = {i : [] for i in range(n)}
    for u, v, w in vertex_list:
        adj[u].append([v,w])
        adj[v].append([u,w])

