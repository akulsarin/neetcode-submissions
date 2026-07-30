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
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result, visited = set(), set()

        def dfs(r: int, c: int, trieNode: TrieNode, wordSoFar: str) -> None:
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or board[r][c] not in trieNode.children:
                return

            visited.add((r, c))
            wordSoFar += board[r][c]
            nextNode = trieNode.children[board[r][c]]

            if nextNode.isWord:
                result.add(wordSoFar)
            
            for nextRow, nextCol in DIRS:
                dfs(r + nextRow, c + nextCol, nextNode, wordSoFar)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)
        