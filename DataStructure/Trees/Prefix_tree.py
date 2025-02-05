class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to map each character to a child node
        self.is_end_of_word = False
    
    def add_child(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]
        
    def set_end_of_word(self):
        self.is_end_of_word = True


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            node = node.add_child(char)
        node.set_end_of_word()
    
    def search(self, word):
        """Returns True if the word exists in the Trie, False otherwise."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Returns True if there is at least one word that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # At least one word starts with this prefix
    
    def delete(self, word):
        """Deletes a word from the Trie if it exists."""
        def _delete(node, word, depth):
            if depth == len(word):  # End of the word
                if not node.is_end_of_word:
                    return False  # Word not found
                node.is_end_of_word = False
                return len(node.children) == 0  # If it is a leaf node, it can be removed
            
            char = word[depth]
            if char not in node.children:
                return False  # Word not present
            
            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False

        _delete(self.root, word, 0)
    
    def autocomplete(self, prefix):
        """Returns all words that start with a given prefix."""
        def _collect_words(node, path, results):
            if node.is_end_of_word:
                results.append(path)
            for char, next_node in node.children.items():
                _collect_words(next_node, path + char, results)

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No words found with this prefix
            node = node.children[char]
        
        words = []
        _collect_words(node, prefix, words)
        return words


# Example usage:
trie = Trie()
trie.insert("house")
trie.insert("home")
trie.insert("hope")
trie.insert("hotel")

print(trie.search("hope"))       # True
print(trie.search("horse"))      # False
print(trie.starts_with("ho"))    # True
print(trie.autocomplete("ho"))   # ['house', 'home', 'hope', 'hotel']
trie.delete("hope")
print(trie.search("hope"))       # False
