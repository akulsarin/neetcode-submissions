class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sChar = s[i]
            if sChar not in sMap:
                sMap[sChar] = 1
            else:
                sMap[sChar] += 1

            tChar = t[i]
            if tChar not in tMap:
                tMap[tChar] = 1
            else:
                tMap[tChar] += 1

        if len(sMap) != len(tMap):
            return False

        for key, val in sMap.items():
            if key not in tMap or val != tMap[key]:
                return False
        
        return True