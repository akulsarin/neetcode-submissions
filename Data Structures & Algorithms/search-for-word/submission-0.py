class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(wordSoFar: List[str], r: int, c: int, visited: set) -> bool:
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited:
                return False

            visited.add((r, c))
            wordSoFar.append(board[r][c])
            if "".join(wordSoFar) == word:
                return True

            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if dfs(wordSoFar, r2, c2, visited):
                    return True

            wordSoFar.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs([], r, c, set()):
                        return True

        return False
        