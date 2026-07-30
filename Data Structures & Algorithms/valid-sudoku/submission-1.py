class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        validItems = {str(i) for i in range(1, 10)}

        # Check rows
        for row in board:
            rowItems = set()
            for item in row:
                if item == ".":
                    continue
                if item not in validItems or item in rowItems:
                    return False
                rowItems.add(item)

        # Check columns
        for c in range(COLS):
            colItems = set()
            for r in range(ROWS):
                item = board[r][c]
                if item == ".":
                    continue
                if item not in validItems or item in colItems:
                    return False
                colItems.add(item)

        # Check Sub-Boxes
        for r in range(3):
            for c in range(3):
                boxStartRow = r * 3
                boxStartCol = c * 3
                subRows = board[boxStartRow : boxStartRow + 3]
                boxItems = set()
                for row in subRows:
                    for colIdx in range(boxStartCol, boxStartCol + 3):
                        item = row[colIdx]
                        if item == ".":
                            continue
                        if item not in validItems or item in boxItems:
                            return False
                        boxItems.add(item)

        return True