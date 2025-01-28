def reverse_linked_list(head):
    previous = None
    current = head
    
    while current:
        next_node = current.next  # Salva il riferimento al nodo successivo
        current.next = previous  # Inverte il collegamento
        previous = current       # Avanza il puntatore precedente
        current = next_node      # Avanza al nodo successivo
    
    return previous