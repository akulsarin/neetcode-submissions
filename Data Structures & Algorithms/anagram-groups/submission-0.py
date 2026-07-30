class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            charCounts = [0] * 26
            for char in string:
                charIdx = ord(char) - ord('a')
                charCounts[charIdx] += 1
            
            anagrams[tuple(charCounts)].append(string)

        return list(anagrams.values())