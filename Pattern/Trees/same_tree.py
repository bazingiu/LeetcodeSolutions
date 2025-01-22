def is_same_tree(node1, node2):
    """
    Determines if two binary trees are identical.
    Args:
        node1 (TreeNode): The root node of the first binary tree.
        node2 (TreeNode): The root node of the second binary tree.
    Returns:
        bool: True if both binary trees are identical, False otherwise.
    The trees are considered identical if they are structurally identical and the nodes have the same value.
    Time Complexity: O(n), where n is the number of nodes in the tree. This is because each node is visited once.
    Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack.
    """
    # Case 1: both nodes are null (i.e., both are empty)
    if not node1 and not node2:
        return True  # The trees are identical (both empty at this point)
    
    # Case 2: both nodes are present and have the same value
    if node1 and node2 and node1.val == node2.val:
        # Recursively check the left and right children
        return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)
    
    # Case 3: one of the nodes is null or the values do not match
    else:
        return False