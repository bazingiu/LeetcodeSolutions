from collections import deque
from typing import Optional, List

class Solution:
    """
    A class used to represent the solution for the problem of finding the right side view of a binary tree.
    Methods
    -------
    rightSideView(root: Optional[TreeNode]) -> List[int]
        Returns a list of integers representing the values of the nodes that are visible from the right side of the binary tree.
    Complexity
    ----------
    Time complexity: O(n), where n is the number of nodes in the binary tree. Each node is processed exactly once.
    Space complexity: O(n), where n is the number of nodes in the binary tree. This is due to the space required for the queue and the output list.
    """
    def rightSideView(self, root) -> List[int]:
        if not root:
            return []

        right_view = []
        node_queue = deque([root])  # Initialize the queue with the root node

        while node_queue:
            level_length = len(node_queue)
            for i in range(level_length):
                current_node = node_queue.popleft()
                
                # Add the node's value if it is the last node of the level
                if i == level_length - 1:
                    right_view.append(current_node.val)
                
                # Add left child first, then right child to the queue
                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

        return right_view
