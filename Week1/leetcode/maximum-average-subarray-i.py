class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wSum = sum(nums[:k])
        maxAvg = wSum/k

        for i in range(len(nums)-k):
            wSum = wSum-nums[i]+nums[i+k]
            maxAvg = max(maxAvg, wSum/k)

        return maxAvg