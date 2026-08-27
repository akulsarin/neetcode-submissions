class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def longest_palindrome_from(l: int, r: int) -> Tuple[int, int]:
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        max_length = 0
        max_l = max_r = 0
        for i in range(N):
            curr_l, curr_r = longest_palindrome_from(i, i)
            curr_len = curr_r - curr_l + 1
            if curr_len > max_length:
                max_length = curr_len
                max_l, max_r = curr_l, curr_r

            curr_l, curr_r = longest_palindrome_from(i, i + 1)
            curr_len = curr_r - curr_l + 1
            if curr_len > max_length:
                max_length = curr_len
                max_l, max_r = curr_l, curr_r

        return s[max_l : max_r + 1]