class DictNode:
    def __init__(self):
        self.children = defaultdict(DictNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = DictNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(node: DictNode, i: int) -> bool:
            if i == n:
                return node.is_word
            
            if word[i] != ".": 
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
            
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False
        
        return dfs(self.root, 0)