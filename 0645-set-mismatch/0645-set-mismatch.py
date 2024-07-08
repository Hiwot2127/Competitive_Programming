class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        m = s - sum(set(nums))
        d = sum(nums) + m - s
        return [d, m]