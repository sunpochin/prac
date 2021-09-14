class Solution:
    def tribonacci(self, n: int) -> int:
        if (0 == n):
            return 0
        if (1 == n):
            return 1
        if (2 == n):
            return 1
        
        dp = [None] * (n + 1)
        # all as define in the problem statement.
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for it in range(3, n+1):
            dp[it] = dp[it-1] + dp[it-2] + dp[it-3]
            
        return dp[n]
