class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zeros = 0
        ones = 0

        for char in s:
            if char == '0':
                zeros += 1
            else:
                ones += 1

        for i in range(1, len(s)):
            left_zeros = s[:i].count('0')
            right_ones = s[i:].count('1')
            score = left_zeros + right_ones
            max_score = max(max_score, score)

        return max_score