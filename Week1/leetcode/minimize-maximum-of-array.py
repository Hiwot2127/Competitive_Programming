class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum,maxim=0,0

        for i, num in enumerate(nums, start=1):
            cum+=num
            maxim=max(ceil(cum/i), maxim)
        return maxim