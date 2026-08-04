class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0

        def validTransform(word1: str, word2: str) -> bool:
            numDiffs = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    numDiffs += 1
            return numDiffs == 1

        numSteps = 0
        queue = deque([beginWord])
        visit = {beginWord}

        while queue:
            numSteps += 1
            for _ in range(len(queue)):
                currWord = queue.popleft()
                if currWord == endWord:
                    return numSteps
                for nextWord in wordList:
                    if nextWord not in visit and validTransform(currWord, nextWord):
                        queue.append(nextWord)
                        visit.add(nextWord)

        return 0
        