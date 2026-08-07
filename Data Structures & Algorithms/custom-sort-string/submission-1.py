class Solution:
    def customSortString(self, order: str, s: str) -> str:
        positions = defaultdict(int)
        result = []
        orderChars = {c for c in order}
        for i, c in enumerate(s):
            positions[c] += 1
            if c not in orderChars:
                result.append(c)

        i = j = 0
        while j < len(order):
            char = order[j]
            if char in positions:
                for _ in range(positions[char]):
                    result.append(char)
            j += 1

        return "".join(result)        