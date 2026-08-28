class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        def valid_transform(word_1: str, word_2: str):
            diffs = 0
            for i in range(len(word_1)):
                if word_1[i] != word_2[i]:
                    diffs += 1
            return diffs == 1

        num_transforms = 0
        queue = deque([beginWord])
        visited = {beginWord}

        while queue:
            num_transforms += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return num_transforms
                for next_word in wordList:
                    if next_word not in visited and valid_transform(word, next_word):
                        queue.append(next_word)
                        visited.add(next_word)

        return 0