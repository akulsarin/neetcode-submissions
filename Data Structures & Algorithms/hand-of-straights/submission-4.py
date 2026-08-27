class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        hand.sort()
        if N % groupSize != 0:
            return False
        
        counts = Counter(hand)
        for num in hand:
            if counts[num] == 0 or counts[num - 1] > 0:
                continue
            
            for i in range(groupSize):
                if counts[num + i] > 0:
                    counts[num + i] -= 1
                else:
                    return False

        return sum(counts.values()) == 0