class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS, COLS = len(picture), len(picture[0])

        rowCounts = defaultdict(int)
        colCounts = defaultdict(int)
        candidates = set()

        for r in range(ROWS):
            for c in range(COLS):
                pixel = picture[r][c]
                if pixel == "B":
                    rowCounts[r] += 1
                    colCounts[c] += 1
                    candidates.add((r, c))

        result = len(candidates)
        for r, c in candidates:
            if rowCounts[r] > 1 or colCounts[c] > 1:
                result -= 1
        
        return result
        