class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prev=float('inf')
        mid=float('inf')

        for i in range(len(nums)):
            if nums[i]<prev:
                prev=min(nums[i], prev)
            if nums[i]>prev:
               mid=min(nums[i], mid)
            if nums[i]>mid:
                return True



