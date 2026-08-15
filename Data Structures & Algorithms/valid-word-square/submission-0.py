class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            newWord = []
            for w in words:
                if i < len(w):
                    newWord.append(w[i])
            if "".join(newWord) != word:
                return False
        return True