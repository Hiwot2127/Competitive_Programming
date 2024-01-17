class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        pre=1
        post=1
        
        for i in range(len(nums)):
            arr[i]*=pre
            pre= pre*nums[i]
            arr[len(nums)-i-1]*= post
            post= post*nums[len(nums)-i-1]
        return arr



