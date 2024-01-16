class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        check=0
        for i in range (len(nums)):
            check+=nums[i]
            ans.append(check)
        return ans