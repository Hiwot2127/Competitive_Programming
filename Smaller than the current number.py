class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1=sorted(nums)
        res=[]
        for num in nums:
            count=nums1.index(num)
            res.append(count)
        return res
