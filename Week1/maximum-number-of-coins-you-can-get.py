class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total_coins = 0
        for i in range( len(piles)//3):
            total_coins += piles[-2-2*i]
        return total_coins