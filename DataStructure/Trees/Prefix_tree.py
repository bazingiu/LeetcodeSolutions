class PrefixNode:
    def __init__(self):
        self.childs = {}  # Dizionario per mappare ogni carattere a un nodo figlio
        self.is_end_of_word = False
    
    def add_child(self, char):
        # Aggiungi un nodo figlio se non esiste già
        if char not in self.childs:
            self.childs[char] = PrefixNode()
        return self.childs[char]
        
    def set_end_of_word(self):  # Aggiungi `self` come primo parametro
        self.is_end_of_word = True


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.add_child(char)  # Naviga o crea i nodi figli
        node.set_end_of_word()  # Imposta l'ultimo nodo come fine della parola