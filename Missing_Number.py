class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n * (n + 1)) // 2  
        current_sum = sum(nums)  
        missing_number = total_sum - current_sum
        return missing_number
    
