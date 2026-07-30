class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min([len(string) for string in strs])
        lcp = ""
        for i in range(shortest):
            char = strs[0][i]
            for string in strs[1:]:
                if string[i] != char:
                    return lcp
            lcp += char
        return lcp



        