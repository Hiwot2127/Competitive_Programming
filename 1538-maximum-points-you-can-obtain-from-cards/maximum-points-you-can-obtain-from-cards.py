class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        window_sum = sum(cardPoints[:n - k])
        max_sum = total_sum - window_sum
        left = 0

        for right in range(n - k, n):
            window_sum -= cardPoints[left]
            window_sum += cardPoints[right]
            max_sum = max(max_sum, total_sum - window_sum)
            left += 1

        return max_sum