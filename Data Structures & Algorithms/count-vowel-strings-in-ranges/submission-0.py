class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefixSum = []
        for i, word in enumerate(words):
            prev = prefixSum[i - 1] if i > 0 else 0
            prefixSum.append(prev)
            if word[0] in vowels and word[-1] in vowels:
                prefixSum[-1] += 1

        result = []
        for l, r in queries:
            lVal = 0 if l == 0 else prefixSum[l - 1]
            rVal = prefixSum[r]
            result.append(rVal - lVal)
        return result
                

        