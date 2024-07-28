class Solution:
    def reachNumber(self, target: int) -> int:
        res, k = 0, 0
        target = abs(target)
        while res < target:
            res += k
            k += 1
        while (res - target) % 2:
            res += k
            k += 1
        return k - 1 