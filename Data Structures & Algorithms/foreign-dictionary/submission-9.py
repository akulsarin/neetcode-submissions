class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {c for word in words for c in word}
        adj = defaultdict(set)
        inDegree = defaultdict(int)
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            for aChar, bChar in zip(a, b):
                if aChar != bChar:
                    if bChar not in adj[aChar]:
                        adj[aChar].add(bChar)
                        inDegree[bChar] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        
        queue = deque([char for char in chars if inDegree[char] == 0])
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for nextChar in adj[char]:
                inDegree[nextChar] -= 1
                if inDegree[nextChar] == 0:
                    queue.append(nextChar)

        if len(result) != len(chars):
            return ""

        return "".join(result)