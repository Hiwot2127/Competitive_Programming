class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_value = float('inf')
        
        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            min_value = min(min_value, num)
            stack.append([num, min_value])
        
        return False
            