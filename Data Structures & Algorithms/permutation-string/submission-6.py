class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return False

        s1Count = Counter(s1)
        s2Count = defaultdict(int)
        
        matched = 0
        matchTarget = len(s1Count)

        for i in range(M):
            char = s2[i]
            s2Count[char] += 1
            if char in s1Count: 
                if s2Count[char] == s1Count[char]:
                    matched += 1
                elif s2Count[char] == s1Count[char] + 1:
                    matched -= 1

        for i in range(M, N):
            if matched == matchTarget:
                return True

            removeChar = s2[i - M]
            s2Count[removeChar] -= 1
            if removeChar in s1Count:
                if s2Count[removeChar] == s1Count[removeChar]:
                    matched += 1
                elif s2Count[removeChar] == s1Count[removeChar] - 1:
                    matched -= 1
            
            insertChar = s2[i]
            s2Count[insertChar] += 1
            if insertChar in s1Count:
                if s2Count[insertChar] == s1Count[insertChar]:
                    matched += 1
                elif s2Count[insertChar] == s1Count[insertChar] + 1:
                    matched -= 1
                    
        return matched == matchTarget