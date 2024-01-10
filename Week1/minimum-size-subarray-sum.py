class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        start = 0
        min_size = float('inf')
        sum = 0
        
        for end, number in enumerate(nums):
            
            sum += number
            
            while sum >= s:

                min_size = min( min_size, end - start + 1)
                sum -= nums[start]
                
                start += 1
                
        
        if min_size == float('inf'):

            return 0
        
        else:
            
            return min_size
                