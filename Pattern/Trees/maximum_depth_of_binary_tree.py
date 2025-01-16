# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root):
    """
    Calculate the maximum depth of a binary tree.
    Args:
        root (TreeNode): The root node of the binary tree.
    Returns:
        int: The maximum depth of the binary tree.
    Time Complexity: O(n), where n is the number of nodes in the binary tree.
    Space Complexity: O(h), where h is the height of the binary tree due to the recursion stack.
    """
    # If the node is null, the tree (or subtree) has a depth of 0
    if not root:
        return 0
        
    # Calculate the maximum depth of the left and right children and add 1 for the current node
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
