class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.word = True
        

    def search(self, word: str) -> bool:
        N = len(word)
        queue = deque([self.root])
        i = 0

        while queue and i < N:
            currChar = word[i]
            for _ in range(len(queue)):
                node = queue.popleft() 
                if currChar == ".":
                    if i == N - 1 and any([child.word for child in node.children.values()]):
                        return True
                    queue.extend(node.children.values())
                elif currChar in node.children:
                    if i == N - 1 and currChar in node.children and node.children[currChar].word:
                        return True
                    queue.append(node.children[currChar])
            i += 1

        return False
                    

        
