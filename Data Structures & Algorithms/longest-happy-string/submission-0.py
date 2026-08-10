class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if max(a, b, c) == 0:
            return ""

        charMap = {"a": a, "b": b, "c": c}
        remaining = []
        for char, freq in charMap.items():
            if freq != 0:
                heapq.heappush(remaining, (-freq, char))


        res = []
        while remaining:
            if len(remaining) == 1:
                freq, char = heapq.heappop(remaining)
                freq *= -1
                for _ in range(min(2, freq)):
                    res.append(char)
                break
            
            freq, char = heapq.heappop(remaining)

            lastTwo = res[-2:]
            if len(lastTwo) == 2 and res[-2] == res[-1] == char:
                freq2, char2 = heapq.heappop(remaining)
                res.append(char2)
                if freq2 + 1 != 0:
                    heapq.heappush(remaining, (freq2 + 1, char2))
            else: 
                res.append(char)
                freq += 1

            if freq != 0:
                heapq.heappush(remaining, (freq, char))

        return "".join(res)

            

            
            




        