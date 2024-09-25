class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        start = sorted(start)

        def check(th: int):
            prev = start[0]
            for i in range(1, n):
                current = prev + th

                if current <= start[i]:
                    prev = start[i]
                elif current > start[i] + d:
                    return False
                else:
                    prev = current
            return True

        left, right = 0, d + max(start) - min(start)
        while left < right:
            mid = left + (right - left) // 2 + 1

            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left