class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur = 0
        maxs = float('-inf')
        unique = set()
        left=0

        for right in range(len(nums)):

            while nums[right] in unique:
                cur-=nums[left]
                unique.remove(nums[left])
                left+=1
            unique.add(nums[right])
            cur += nums[right]
            maxs = max(maxs, cur)

        return maxs