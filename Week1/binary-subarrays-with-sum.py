class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_counts = {0: 1}  

        for num in nums:
            cumulative_sum += num
            difference = cumulative_sum - goal
            if difference in sum_counts:
                count += sum_counts[difference]
            if cumulative_sum in sum_counts:
                sum_counts[cumulative_sum] += 1
            else:
                sum_counts[cumulative_sum] = 1

        return count

