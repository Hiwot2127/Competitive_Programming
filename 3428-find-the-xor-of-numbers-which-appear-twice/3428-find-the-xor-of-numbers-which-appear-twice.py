class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        box=set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in box:
                res^=nums[i]
            else:
                box.add(nums[i])
        return res
