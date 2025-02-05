from collections import deque

def level_order_traversal(root):
    # Time complexity: O(n), where n is the number of nodes in the binary tree.
    # Space complexity: O(n), due to the storage required for the output list and the queue.
    if not root:
        return []

    levels = []
    nodes_queue = deque([root])  # Usa deque per la coda
    while nodes_queue:
        level_length = len(nodes_queue)
        current_level = []
        for _ in range(level_length):
            current_node = nodes_queue.popleft()  # popleft() è O(1)
            current_level.append(current_node.val)
            if current_node.left:
                nodes_queue.append(current_node.left)
            if current_node.right:
                nodes_queue.append(current_node.right)
        levels.append(current_level)
    return levels