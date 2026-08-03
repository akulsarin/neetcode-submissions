class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        currNode = self
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            currNode = currNode.children[c]
        currNode.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTree = TrieNode()
        for word in words:
            prefixTree.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        result = []

        def dfs(r: int, c: int, wordSoFar: List[str], node: TrieNode, visit: set) -> None:
            if (r, c) in visit or min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] not in node.children:
                return

            currChar = board[r][c]
            visit.add((r, c))
            wordSoFar.append(currChar)
            nextNode = node.children[currChar]
                
            if nextNode.isWord:
                nextNode.isWord = False
                result.append("".join(wordSoFar))

            for dr, dc in DIRS:
                dfs(r + dr, c + dc, wordSoFar, nextNode, visit)

            wordSoFar.pop()
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, [], prefixTree, set())

        return result