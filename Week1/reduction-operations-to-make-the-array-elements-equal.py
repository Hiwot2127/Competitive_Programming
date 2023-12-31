class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        operations = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev: 
                continue
            
            if nums[i] < prev:
                operations += i
            prev = nums[i]

        return operations