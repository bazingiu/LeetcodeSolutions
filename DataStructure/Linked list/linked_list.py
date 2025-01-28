class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Aggiunge un nuovo nodo in coda."""
        new_node = Node(value)
        if not self.head:  # Lista vuota
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Vai all'ultimo nodo
                current = current.next
            current.next = new_node

    def insert(self, value, position):
        """Inserisce un nodo in una posizione specifica."""
        if position < 0:
            raise ValueError("La posizione deve essere >= 0")
        new_node = Node(value)
        if position == 0:  # Inserisci in testa
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            index = 0
            while current and index < position:
                prev = current
                current = current.next
                index += 1
            if index != position:
                raise IndexError("Posizione fuori dai limiti")
            prev.next = new_node
            new_node.next = current

    def remove(self, value):
        """Rimuove il primo nodo che contiene il valore specificato."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:  # Nodo non è la testa
                    prev.next = current.next
                else:  # Nodo è la testa
                    self.head = current.next
                return  # Esce dopo la rimozione
            prev = current
            current = current.next
        raise ValueError("Valore non trovato nella lista")

    def find(self, value):
        """Cerca un valore e restituisce l'indice del primo nodo trovato."""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1  # Valore non trovato

    def size(self):
        """Restituisce la dimensione della lista (numero di nodi)."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """Stampa i valori della lista in formato leggibile."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
            
        print(" -> ".join(values))
