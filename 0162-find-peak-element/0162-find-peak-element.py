class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        first,second=0,len(nums)-1
        while first<second:
            mid=first+(second-first)//2
            if nums[mid]>nums[mid+1]:
                second=mid
            else:
                first=mid+1
        return first