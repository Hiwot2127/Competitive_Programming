class Solution:
    def maxDistance(self, a: List[List[int]]) -> int:
        res, minn, maxx = 0, inf, -inf
        for b in a:
            res = max(res, b[-1] - minn, maxx - b[0])
            minn = min(minn, b[0])
            maxx = max(maxx, b[-1])
        return res