class Solution: 
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones_count = 0
        for num in nums:
            if num == 1:
                ones_count += 1
        
        zeros_count, max_division = 0, ones_count
        indices_dict = collections.defaultdict(list)
        indices_dict[ones_count].append(0)
        
        for i, num in enumerate(nums):
            zeros_count += int(num == 0)
            ones_count -= int(num == 1)
            indices_dict[zeros_count + ones_count].append(i + 1)
            max_division = max(max_division, zeros_count + ones_count)
        
        return indices_dict[max_division]