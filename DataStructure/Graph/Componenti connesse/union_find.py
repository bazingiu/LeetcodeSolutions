class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n  # Usato per tenere traccia delle dimensioni o del peso degli alberi

    def find(self, node):
        if self.parent[node] != node:
            # Path compression per accelerare le operazioni successive
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Trova i rappresentanti dei due insiemi
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Se sono già nello stesso insieme, non fare nulla
        if root1 == root2:
            return False

        # Union by rank: collega l'albero più piccolo sotto l'albero più grande
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]

        return True

# Time complexity: O(n ⋅ α(n))
# Space complexity: O(n)