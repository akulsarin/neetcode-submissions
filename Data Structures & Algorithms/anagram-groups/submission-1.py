class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        for string in strs:
            char_counts = [0] * 26
            for char in string:
                idx = ord('a') - ord(char)
                char_counts[idx] += 1
            grouping[tuple(char_counts)].append(string)
        return list(grouping.values())