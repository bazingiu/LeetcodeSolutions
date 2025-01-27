
from binary_search_tree import BinaryTree

tree = BinaryTree()
values = [5, 3, 7, 2, 4, 6, 8]
for val in values:
    tree.insert_node(val)
tree.inorder_traversal()