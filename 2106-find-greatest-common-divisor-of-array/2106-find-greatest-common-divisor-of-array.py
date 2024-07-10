class Solution:
    def findGCD(self, nums: List[int]) -> int:
            sm = min(nums)
            la = max(nums)
            for i in range(sm, 0, -1):
                if sm % i == 0 and la % i == 0:
                    return i