class Solution:
    """
    This class provides a method to calculate the diameter of a binary tree.
    Methods
    -------
    diameterOfBinaryTree(root):
        Calculates the diameter of the binary tree with the given root node.
        The diameter is defined as the length of the longest path between any two nodes in the tree.
    Parameters
    ----------
    root : TreeNode
        The root node of the binary tree.
    Returns
    -------
    int
        The diameter of the binary tree.
    Notes
    -----
    - The function uses a helper function `height` to calculate the height of the tree and update the diameter.
    - The diameter is updated as the maximum value of the current diameter and the sum of the heights of the left and right subtrees.
    - The height of a node is defined as 1 plus the maximum height of its left and right subtrees.
    # Complessità temporale: O(n), dove n è il numero di nodi nell'albero.
    # Complessità spaziale: O(h), dove h è l'altezza dell'albero, a causa della ricorsione sulla pila.
    """
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter