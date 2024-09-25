class Solution:
    def nthUglyNumber(self, num: int) -> int:
        ugly_numbers = [1]
        heap = []
        for prime in [2, 3, 5]:
            heapq.heappush(heap, (prime, prime, 0))
        
        while len(ugly_numbers) < num:
            next_ugly, prime, idx = heapq.heappop(heap)
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
            heapq.heappush(heap, (prime * ugly_numbers[idx + 1], prime, idx + 1))
        
        return ugly_numbers[-1]