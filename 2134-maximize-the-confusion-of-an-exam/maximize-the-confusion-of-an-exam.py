class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        left = 0
        right = 0
        max_beauty = 0
        freq = {'T': 0, 'F': 0}

        while right < n:
            freq[answerKey[right]] += 1
            max_count = max(freq.values())

            if (right - left + 1) - max_count > k:
                freq[answerKey[left]] -= 1
                left += 1

            max_beauty = max(max_beauty, right - left + 1)
            right += 1

        return max_beauty