class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def _print_trie_helper(self, node, word):
        if node.is_end_of_word:
            print(word)
        for char, child_node in node.children.items():
            self._print_trie_helper(child_node, word + char)
            
    def print_trie(self):
        self._print_trie_helper(self.root, "")

# Crea un trie
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("ap")
trie.insert("a")
trie.print_trie()
