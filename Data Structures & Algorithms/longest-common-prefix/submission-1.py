class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_longest = strs[0]
        for string in strs:
            if curr_longest.startswith(string):
                curr_longest = string
            elif not string.startswith(curr_longest):
                new_longest = ""
                for i, c in enumerate(curr_longest):
                    if i == len(string) or string[i] != c:
                        break
                    new_longest += c
                curr_longest = new_longest
        return curr_longest