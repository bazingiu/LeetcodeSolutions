class Solution:
    def lowestCommonAncestor(self, root, node1, node2):
        while root:
            # If both node1 and node2 are smaller than root, go left
            if node1.val < root.val and node2.val < root.val:
                root = root.left
            # If both node1 and node2 are greater than root, go right
            elif node1.val > root.val and node2.val > root.val:
                root = root.right
            # If root is between node1 and node2, then it's the LCA
            else:
                return root

# La complessità temporale di questo codice è O(h), dove h è l'altezza dell'albero.
# La complessità spaziale è O(1) poiché non viene utilizzata memoria aggiuntiva significativa.