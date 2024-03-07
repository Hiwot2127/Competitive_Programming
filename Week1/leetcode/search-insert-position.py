class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        m=-1

        while l<=r:
            m=(l+r)//2
            if target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
            else:
                return m
        return r+1
