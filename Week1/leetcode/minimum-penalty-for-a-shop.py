class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_s = 0
        s= 0
        hour = -1

        for i, c in enumerate(customers):
            s += 1 if c == 'Y' else -1
            if s > max_s:
                max_s= s
                hour = i
        return hour + 1