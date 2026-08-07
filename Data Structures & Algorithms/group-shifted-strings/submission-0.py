class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getHash(string: str) -> str:
            res = []
            for i in range(len(string) - 1):
                diff = ord('a') + (ord(string[i + 1]) - ord(string[i])) % 26
                res.append(str(diff))
            return "#".join(res)

        groups = defaultdict(list)
        for string in strings:
            groups[getHash(string)].append(string)
        
        return list(groups.values())

        