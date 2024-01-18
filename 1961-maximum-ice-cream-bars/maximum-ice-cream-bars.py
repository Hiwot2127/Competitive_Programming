class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_price = max(costs)
        freq = [0] * (max_price + 1)

        for cost in costs:
            freq[cost] += 1

        total = 0
        for price in range(1, max_price + 1):
            if coins >= price:
                num_bars = min(freq[price], coins // price)
                total += num_bars
                coins -= num_bars * price
            else:
                break

        return total