class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for a, b in zip(w1, w2):
                if a != b:
                    adj[a].add(b)
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        state = {}
        result = []

        def dfs(c: str) -> bool:
            if c in state:
                return state[c]

            state[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            state[c] = False

            result.append(c)
            return False

        for c in adj:
            if dfs(c):
                return ""

        result.reverse()
        return "".join(result)
        