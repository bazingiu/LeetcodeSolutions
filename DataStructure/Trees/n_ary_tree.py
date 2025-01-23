class Node:
    def __init__(self, val = 0, children = None):
        self.val = val
        self.children = children if children is not None else []
    
class NTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_node(self.root, val)
    