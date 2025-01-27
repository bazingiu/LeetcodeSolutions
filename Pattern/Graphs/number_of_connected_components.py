class DSU:
    def __init__(self, n):
        # Ogni nodo è inizialmente il proprio genitore
        self.parent = list(range(n))
        # Rank inizialmente pari a 1 per ogni nodo
        self.rank = [1] * n

    def find(self, node):
        # Path compression: collega il nodo direttamente al rappresentante del suo insieme
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Trova i rappresentanti dei due nodi
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Se sono già nello stesso insieme, ritorna False
        if root1 == root2:
            return False

        # Unione basata sul rank
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:  # Incrementa il rank solo se uguali
                self.rank[root2] += 1

        return True


def num_of_undirected_components(n, edges):
    # Inizializza il DSU
    dsu = DSU(n)
    components = n

    # Itera su tutti gli archi
    for node1, node2 in edges:
        # Riduci il conteggio dei componenti solo se due nodi vengono uniti
        if dsu.union(node1, node2):
            components -= 1

    return components

# Time complexity: 
# each operation of find or union has a complexity of O(alpha(N)) ackerman inverse
# we iterate trhough E arch
# O(E * alpa(N))

#Space complexity: O(N) 
