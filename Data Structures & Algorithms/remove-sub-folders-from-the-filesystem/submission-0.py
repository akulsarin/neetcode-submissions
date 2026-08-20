class PrefixNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def addFolder(self, folder: str):
        names = folder.split("/")
        curr = self.root
        
        for name in names:
            if not name: 
                continue
            if name not in curr.children:
                curr.children[name] = PrefixNode()
            curr = curr.children[name]
        
        curr.word = True

    def isSubFolder(self, folder: str) -> bool:
        names = folder.split("/")
        curr = self.root
        n = len(names)

        for i, name in enumerate(names):
            if not name: 
                continue
            curr = curr.children[name]
            if curr.word:
                return i != n - 1

        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = PrefixTree()
        for f in folder:
            trie.addFolder(f)

        res = []
        for f in folder:
            if not trie.isSubFolder(f):
                res.append(f)

        return res