class Solution:
    def climbStairs(self, n: int, memo=None) -> int:
        # Initialize the memoization dictionary on the first call
        if memo is None:
            memo = {}
            
        # Base cases
        if n <= 2:
            return n
            
        # Check if we've already calculated the answer for this 'n'
        if n in memo:
            return memo[n]
            
        # If not, calculate it using your recursive logic, but pass the memo along
        op1 = self.climbStairs(n - 1, memo)
        op2 = self.climbStairs(n - 2, memo)
        
        # Store the result in our cache before returning
        memo[n] = op1 + op2
        return memo[n]
        