class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Contatore per tracciare l'ordine durante la visita
        node_count = 0
        kth_value = None

        def in_order_traversal(node):
            nonlocal node_count, kth_value
            
            # Base case: se il nodo è nullo o il risultato è già trovato
            if not node or kth_value is not None:
                return
            
            # Visita il sottoalbero sinistro
            in_order_traversal(node.left)
            
            # Incrementa il contatore durante la visita del nodo corrente
            node_count += 1
            if node_count == k:
                kth_value = node.val
                return
            
            # Visita il sottoalbero destro
            in_order_traversal(node.right)
        
        # Avvia la visita in-order a partire dalla radice
        in_order_traversal(root)
        return kth_value

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Variabile per tracciare il risultato
        result = self.in_order_traversal(root, k)
        return result

    def in_order_traversal(self, node: Optional[TreeNode], k: int) -> int:
        # Pila per simulare il traversal in-order iterativamente
        stack = []
        current_node = node
        count = 0

        # Itera finché ci sono nodi da visitare
        while stack or current_node:
            # Vai sempre più a sinistra
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            # Visita il nodo più a sinistra
            current_node = stack.pop()
            count += 1

            # Se il contatore corrisponde a k, restituisci il valore del nodo
            if count == k:
                return current_node.val
            
            # Passa al sottoalbero destro
            current_node = current_node.right
        
        # In caso di albero malformato o k fuori range
        return -1
