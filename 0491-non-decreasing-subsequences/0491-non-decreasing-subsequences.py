class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def sol(curr, nums):
            if( len(curr) >= 2 and curr[-1] < curr[-2] ): 
                return
            if( len(curr) >= 2 and curr[:] not in res):
                res.add(curr[:])
            for i in range(len(nums)):
                sol( curr + (nums[i],), nums[i+1:] )  
        res = set()
        sol( (), nums)
        return res