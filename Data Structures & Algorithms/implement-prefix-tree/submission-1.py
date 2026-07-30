class PrefixTree:
    class TreeNode:
        def __init__(self):
            self.children = {}
            self.word = False

    def __init__(self):
        self.root = self.TreeNode()
        

    def insert(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = self.TreeNode()
            currNode = currNode.children[c]
        currNode.word = True


    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return currNode.word
        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True

        
        