class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        ROWS = {i for i in range(n)}
        COLS = {i for i in range(n)}
        BOARD = [["."] * n for _ in range(n)]

        def dfs(r: int, colsUsed: set, diagsUsed: set, offDiagsUsed: set) -> None:
            if r == n:
                result.append(["".join(res) for res in BOARD])
                return

            colsAvailable = COLS - colsUsed

            for c in colsAvailable:
                diag = r - c
                offDiag = r + c

                if diag in diagsUsed or offDiag in offDiagsUsed:
                    continue

                colsUsed.add(c)
                diagsUsed.add(diag)
                offDiagsUsed.add(offDiag)
                BOARD[r][c] = "Q"

                dfs(r + 1, colsUsed, diagsUsed, offDiagsUsed)

                BOARD[r][c] = "."
                offDiagsUsed.remove(offDiag)
                diagsUsed.remove(diag)
                colsUsed.remove(c)

        dfs(0, set(), set(), set())
        return result