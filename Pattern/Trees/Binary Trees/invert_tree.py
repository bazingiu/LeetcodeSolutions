def invert_tree(self, root):
    """
    Inverts a binary tree by swapping the left and right children of all nodes.
    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
    Returns:
        Optional[TreeNode]: The root node of the inverted binary tree.
    Time Complexity: O(n), where n is the number of nodes in the tree.
    Space Complexity: O(h), where h is the height of the tree due to the recursion stack.
    """
    if root is None:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right children
    self.invert_tree(root.left)
    self.invert_tree(root.right)

    # Return the root of the inverted tree
    return root