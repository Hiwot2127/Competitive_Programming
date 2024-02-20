class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        g=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=g:
                g=i
        return True if g==0 else False