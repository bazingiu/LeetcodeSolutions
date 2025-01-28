from collections import deque

def zigzagLevelOrder(self, root):
    if not root:
        return []
    
    res = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        res.append(list(level))
        left_to_right = not left_to_right
    
    return res