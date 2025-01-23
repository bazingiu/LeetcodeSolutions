# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    This class provides a method to count the number of "good" nodes in a binary tree.
    A node X in the binary tree is named "good" if in the path from the root to X there are no nodes with a value greater than X.
    Methods
    -------
    goodNodes(root: TreeNode) -> int
        Returns the number of good nodes in the binary tree.
        Parameters:
        root (TreeNode): The root node of the binary tree.
        Returns:
        int: The number of good nodes in the binary tree.
        Time Complexity: O(N), where N is the number of nodes in the binary tree. Each node is visited once.
        Space Complexity: O(H), where H is the height of the binary tree. This space is used by the recursion stack.
    """
    def goodNodes(self, root):

        def dfs(node, max_val):
            if not node:
                return 0

            result = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return result + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)