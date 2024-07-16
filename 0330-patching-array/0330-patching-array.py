class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        val = 1
        m = len(nums)
        i = 0
        while val <= n:
            if i < m and nums[i] <= val:
                val += nums[i]
                i += 1
            else:
                val +=val
                res += 1
        
        return res