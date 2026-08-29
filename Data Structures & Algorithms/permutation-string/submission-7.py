class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if N < M:
            return False
        
        s1_freqs = Counter(s1)
        s2_freqs = defaultdict(int)
        matches = 0
        for r, r_char in enumerate(s2):
            s2_freqs[r_char] += 1
            if s2_freqs[r_char] == s1_freqs[r_char]:
                matches += 1
            elif s2_freqs[r_char] == s1_freqs[r_char] + 1:
                matches -= 1
            
            if r >= M:
                l_char = s2[r - M]
                s2_freqs[l_char] -= 1
                if s2_freqs[l_char] == s1_freqs[l_char]:
                    matches += 1
                elif s2_freqs[l_char] == s1_freqs[l_char] - 1:
                    matches -= 1
            
            if matches == len(s1_freqs):
                return True
        
        return False