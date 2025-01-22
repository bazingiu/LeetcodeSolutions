def is_balanced(root):
    """
    Determines if a binary tree is height-balanced.

    A binary tree is height-balanced if for every node in the tree, 
    the height difference between the left and right subtrees is at most 1.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        bool: True if the binary tree is height-balanced, False otherwise.

    Time Complexity: O(n), where n is the number of nodes in the binary tree.
    Space Complexity: O(h), where h is the height of the binary tree due to the recursion stack.
    """
    def get_height(node):
        if not node:
            return 0
        left_subtree_height = get_height(node.left)
        right_subtree_height = get_height(node.right)
        if left_subtree_height == -1 or right_subtree_height == -1 or abs(left_subtree_height - right_subtree_height) > 1:
            return -1
        return max(left_subtree_height, right_subtree_height) + 1
    return get_height(root) != -1