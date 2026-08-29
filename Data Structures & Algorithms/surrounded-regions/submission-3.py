class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if r in {0, rows - 1} or c in {0, cols - 1}:
                    if board[r][c] == "O":
                        queue.append((r, c))        
                        visit.add((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                r2, c2 = r + dr, c + dc
                if (
                    0 <= r2 < rows 
                    and 0 <= c2 < cols 
                    and (r2, c2) not in visit 
                    and board[r2][c2] == "O"
                ):
                    queue.append((r2, c2))
                    visit.add((r2, c2))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"