class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        cur=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                cur=max(count, cur)
                count=0
        cur=max(count, cur)
        return cur


