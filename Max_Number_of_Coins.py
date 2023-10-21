class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        lp = len(piles)
        res = 0
      
        for i in range(lp //3):
            piles.pop()
            res += piles.pop()
          
        return res
