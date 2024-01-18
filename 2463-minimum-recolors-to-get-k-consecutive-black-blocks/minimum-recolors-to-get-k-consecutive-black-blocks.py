class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_ops = float('inf')
        black_count = 0
        window_start = 0

        for i in range(n):
            if blocks[i] == 'B':
                black_count += 1

            if i - window_start + 1 > k:
                if blocks[window_start] == 'B':
                    black_count -= 1
                window_start += 1

            if i - window_start + 1 == k:
                min_ops = min(min_ops, k - black_count)
                if blocks[window_start] == 'B':
                    black_count -= 1
                window_start += 1

        if min_ops == float('inf'):
            return 0
        else:
            return min_ops