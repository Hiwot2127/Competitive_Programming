class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp=[set() for _ in range(len(stones))]
        dp[0].add(1)
        for i in range (1,len(stones)):
            for j in range(i):
                dif=stones[i]-stones[j]
                if dif in dp[j]:
                    dp[i].add(dif-1)
                    dp[i].add(dif)
                    dp[i].add(dif+1)
        if len(dp[-1])>0:
            return True
        return False

