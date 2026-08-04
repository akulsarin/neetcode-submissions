class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([])
        visit = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r, 0))
                visit.add((r, 0))
            if board[r][COLS - 1] == "O":
                queue.append((r, COLS - 1))
                visit.add((r, COLS - 1))
        for c in range(1, COLS - 1):
            if board[0][c] == "O":
                queue.append((0, c))
                visit.add((0, c))
            if board[ROWS - 1][c] == "O":
                queue.append((ROWS - 1, c))
                visit.add((ROWS - 1, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop()
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or (r2, c2) in visit or board[r2][c2] == "X":
                        continue
                    queue.append((r2, c2))
                    visit.add((r2, c2))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit:
                    board[r][c] = "X"
        