class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0:
            return False
        
        counts = Counter(hand)
        for num in sorted(counts.keys()):
            while counts[num] > 0:
                for i in range(groupSize):
                    if counts[num + i] > 0:
                        counts[num + i] -= 1
                    else:
                        return False
        return True