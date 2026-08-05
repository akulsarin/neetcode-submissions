class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def palindromeLength(l: int, r: int) -> int:
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return (r - l + 1) - 2

        longest = 0
        longestL, longestR = 0, 0
        for i in range(N):
            longestOdd = palindromeLength(i, i)
            longestEven = palindromeLength(i, i + 1)
            if max(longestOdd, longestEven) > longest:
                longest = max(longestOdd, longestEven)
                if longestOdd > longestEven:
                    width = (longestOdd - 1) // 2
                    longestL, longestR = i - width, i + width
                else:
                    width = (longestEven - 2) // 2
                    longestL, longestR = i - width, i + 1 + width

        return s[longestL : longestR + 1]

        