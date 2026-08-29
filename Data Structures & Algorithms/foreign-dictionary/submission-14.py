class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}
        in_degrees = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if len(word1) < len(word2) and word2.startswith(word1):
                continue
            for j in range(len(word1)):
                if j == len(word2):
                    return ""
                char1, char2 = word1[j], word2[j]
                if char1 != char2:
                    adj[char1].append(char2)
                    in_degrees[char2] += 1
                    break
        
        num_chars = len(set(list("".join(words))))
        queue = deque([char for char in adj if in_degrees[char] == 0])
        char_order = []
        while queue:
            curr_char = queue.popleft()
            char_order.append(curr_char)
            for next_char in adj[curr_char]:
                in_degrees[next_char] -= 1
                if in_degrees[next_char] == 0:
                    queue.append(next_char)
        
        if len(char_order) != num_chars:
            return ""
        
        return "".join(char_order)