class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n,memo):
            if n==0 or n==1:
                return 1
            if n not in memo:
                memo[n]=rec(n-1,memo)+rec(n-2,memo)
            return memo[n]
        memo={}
        return rec(n,memo)

            
