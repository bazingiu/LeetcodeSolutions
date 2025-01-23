class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_node(self.root, val)

    def _insert_node(self, current_node, val):
        if not current_node:
            return Node(val)
        if val < current_node.val:
            current_node.left = self._insert_node(current_node.left, val)
        else:
            current_node.right = self._insert_node(current_node.right, val)
        return current_node
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)
        return result
    
    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])
        
    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result
            
    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])
        
    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)
        return result
