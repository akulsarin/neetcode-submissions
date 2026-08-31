class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # Check rows
        for r in board:
            seen = set()
            for digit in r:
                if digit != "." and digit in seen:
                    return False
                seen.add(digit)
        
        # Check cols
        for c in range(COLS):
            seen = set()
            for r in board:
                digit = r[c]
                if digit != "." and digit in seen:
                    return False
                seen.add(digit)

        # Check sub-boxes
        for start_row in range(0, ROWS, 3):
            for start_col in range(0, COLS, 3):
                end_row, end_col = start_row + 3, start_col + 3
                seen = set()
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        digit = board[r][c]
                        if digit != "." and digit in seen:
                            return False
                        seen.add(digit)

        return True   