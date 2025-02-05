# Time complexity: O(V +E)
# Space complexity: O(V)
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # Helper function to perform DFS and determine safe nodes
        def dfs(node):
            if color[node] != 0:
                # If the node is already visited, return whether it's safe
                return color[node] == 2
            # Mark the node as visiting
            color[node] = 1
            # Check all adjacent nodes
            for neighbor in graph[node]:
                # If any neighbor is visiting (cycle) or not safe, this node is unsafe
                if color[neighbor] == 1 or not dfs(neighbor):
                    return False
            # Mark the node as safe
            color[node] = 2
            return True
        
        n = len(graph)
        color = [0] * n  # Colors: 0 = unvisited, 1 = visiting, 2 = safe
        result = []
        
        # Run DFS for all nodes
        for node in range(n):
            if dfs(node):
                result.append(node)
        
        return result
