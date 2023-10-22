class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        def reverse(left,right,nums):

            while left <right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            return nums
        
        nums = reverse(0,len(nums)-1,nums) 
        nums = reverse(0,k-1,nums) 
        nums = reverse(k,len(nums)-1,nums) 

        return nums
