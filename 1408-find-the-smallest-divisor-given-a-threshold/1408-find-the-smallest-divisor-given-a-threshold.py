class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left,right=1,max(nums)
        res=-1

        while left<=right:
            mid=(left+right)//2
            cur=0
            for i in range(len(nums)):
                cur+=ceil(nums[i]/mid)
            if cur<=threshold:
                right=mid-1
                res=mid
            else:
                left=mid+1
        return res

