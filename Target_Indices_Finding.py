class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        ans=[]

        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
        return sorted(ans)
