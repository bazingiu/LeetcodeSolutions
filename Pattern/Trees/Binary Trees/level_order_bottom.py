from collections import deque

def levelOrderBottom(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
from collections import deque
from typing import Optional, List

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        queue = deque([root])  # Inizializza la coda con la radice
        output = deque()  # Usare deque per aggiungere direttamente in testa

        while queue:
            level_nodes = []  # Lista per i nodi del livello corrente
            for _ in range(len(queue)):  # Processa tutti i nodi nel livello
                curr_node = queue.popleft()
                level_nodes.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            output.appendleft(level_nodes)  # Aggiungi il livello in cima al risultato
        
        return list(output)  # Converte deque in lista prima di restituire

# Time complexity: O(N)
# Space complexity: O(N)