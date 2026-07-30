class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case check
        if not t or not s:
            return ""

        # Build target character counts on the fly
        tCharCounts = {}
        for c in t:
            tCharCounts[c] = tCharCounts.get(c, 0) + 1
            
        matchLen = len(tCharCounts)
        matches = 0
        
        # Empty dictionary, we will populate it dynamically
        sCharCounts = {} 

        minL, minR = 0, float('inf')
        l = 0
        
        for r in range(len(s)):
            rChar = s[r]
            # Dynamically add to the dictionary
            sCharCounts[rChar] = sCharCounts.get(rChar, 0) + 1
            
            if rChar in tCharCounts and sCharCounts[rChar] == tCharCounts[rChar]:
                matches += 1
                
            while matches == matchLen:
                lChar = s[l]
                sCharCounts[lChar] -= 1
                
                if lChar in tCharCounts:
                    if r - l < minR - minL:
                        minL, minR = l, r
                    
                    # Check if removing lChar broke our matching condition
                    if sCharCounts[lChar] < tCharCounts[lChar]:
                        matches -= 1
                l += 1
                
        return s[minL : minR + 1] if minR != float('inf') else ""