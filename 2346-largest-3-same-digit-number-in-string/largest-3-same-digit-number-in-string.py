class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""

        for i in range(len(num) - 2):
            current_substring = num[i:i+3]

            if len(set(current_substring)) == 1:
                max_good = max(max_good, current_substring)

        return max_good