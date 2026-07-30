class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2)
        if N1 > N2:
            return False

        s1Chars = {c: 0 for c in s1 + s2}
        s2Chars = {c: 0 for c in s1 + s2}
        
        for i in range(N1):
            c1, c2 = s1[i], s2[i]
            s1Chars[c1] += 1
            s2Chars[c2] += 1

        matches = 0
        for char, count in s1Chars.items():
            if s2Chars[char] == count:
                matches += 1

        l = 0
        matchLen = len(s1Chars)
        for r in range(N1, N2):
            print(s1Chars)
            print(s2Chars)
            print(matches)
            print(matchLen, len(s2Chars))
            if matches == matchLen:
                return True

            lChar, rChar = s2[l], s2[r]

            s2Chars[rChar] += 1
            if s2Chars[rChar] == s1Chars[rChar]:
                matches += 1
            elif s2Chars[rChar] == s1Chars[rChar] + 1:
                matches -= 1

            s2Chars[lChar] -= 1
            if s2Chars[lChar] == s1Chars[lChar]:
                matches += 1
            elif s2Chars[lChar] == s1Chars[lChar] - 1:
                matches -= 1

            l += 1

        return matches == matchLen

            


        