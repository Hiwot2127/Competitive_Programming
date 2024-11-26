class Solution:
    def findMin(self, nums: List[int]) -> int:
            l,r=0,len(nums)-1
       
            while l<=r:
                if nums[l]<=nums[r]:
                    return nums[l]
                m=(l+r)//2
                if nums[l]>nums[m]:
                    r=m
                else: 
                    l=m+1
           
