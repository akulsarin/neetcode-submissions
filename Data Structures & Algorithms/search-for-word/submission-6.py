class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visit = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == N - 1:
                return True
            
            visit.add((r, c))
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or (r2, c2) in visit:
                    continue
                if board[r2][c2] == word[i + 1] and dfs(r2, c2, i + 1):
                    return True
            visit.remove((r, c))

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False