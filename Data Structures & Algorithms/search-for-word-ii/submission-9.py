class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def add_word(self, word):
        curr_node = self
        for char in word:
            curr_node = curr_node.children[char]
        curr_node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        present = set()
        visit = set()

        trie = TrieNode()
        for word in words:
            trie.add_word(word)

        def dfs(r: int, c: int, node: TrieNode, word_so_far: List[str]):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit:
                return
            
            char = board[r][c]
            if char not in node.children:
                return

            visit.add((r, c))
            next_node = node.children[char]
            word_so_far.append(char)
            if next_node.is_word:
                present.add("".join(word_so_far))
            
            for dr, dc in dirs:
                dfs(r + dr, c + dc, next_node, word_so_far)

            visit.remove((r, c))
            word_so_far.pop()
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie, [])
        
        return list(present)