class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)

        edges: List[List[str]] = []

        def addEdges(word1: str, word2: str) -> bool:
            if word1 == word2:
                return True

            # word1 < word2
            i = 0
            while i < min(len(word1), len(word2)):
                if word1[i] != word2[i]:
                    edges.append([word1[i], word2[i]])
                    return True
                i += 1

            return len(word1) < len(word2)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not addEdges(words[i], words[j]):
                    return ""

        adj = defaultdict(set)
        for c1, c2 in edges:
            adj[c1].add(c2)

        visit = set()
        path = set()
        result = []

        def dfs(c: str) -> bool:
            if c in path:
                return False

            if c in visit:
                return True

            visit.add(c)
            path.add(c)

            for neighbor in adj[c]:
                if not dfs(neighbor):
                    return False
            
            path.remove(c)
            result.append(c)

            return True

        for c in chars:
            if not dfs(c):
                return ""

        result.reverse()
        return "".join(result)



            

            

            


        