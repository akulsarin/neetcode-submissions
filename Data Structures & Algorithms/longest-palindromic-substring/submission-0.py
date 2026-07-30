class Solution:
    def longestPalindromeFromPos(self, s: str, l: int, r: int) -> str:
        longest = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            longest = s[l : r + 1]
            l -= 1
            r += 1
        return longest


    def longestPalindrome(self, s: str) -> str:
        currLongest = ""

        for i in range(len(s)):
            # odd length
            l, r = i, i
            longest = self.longestPalindromeFromPos(s, l, r)
            if len(longest) > len(currLongest):
                currLongest = longest
            
            # even length
            l, r = i, i + 1
            longest = self.longestPalindromeFromPos(s, l, r)
            if len(longest) > len(currLongest):
                currLongest = longest

        return currLongest

        