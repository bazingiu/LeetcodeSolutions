from collections import deque

def level_order_traversal(root):
    """
    Perform a level order traversal on an N-ary tree.
    Args:
        root (Node): The root node of the N-ary tree.
    Returns:
        List[List[int]]: A list of lists, where each inner list contains the values of the nodes at that level of the tree.
    Time Complexity:
        O(n), where n is the number of nodes in the tree. Each node is processed exactly once.
    Space Complexity:
        O(n), where n is the number of nodes in the tree. This is due to the space required to store the output and the queue.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            queue.extend(node.children)

        result.append(current_level)

    return result
