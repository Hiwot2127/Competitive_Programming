class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1

        if len(nums)==1 or not nums:
            return len(nums)
    
        while j<len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1