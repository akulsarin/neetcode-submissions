class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result << 1 
            bit = n & (1 << i)
            result = result | (bit >> i)
        return result