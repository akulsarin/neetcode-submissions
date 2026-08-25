class Solution:
    def climbStairs(self, n: int) -> int:
        # Start at first step
        num_prev = 1
        num_curr = 1

        for _ in range(n - 1):
            num_prev, num_curr = num_curr, num_prev + num_curr 
        
        return num_curr 