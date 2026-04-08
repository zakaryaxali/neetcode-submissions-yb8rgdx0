class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTree()
            node = node.children[char]
        node.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)