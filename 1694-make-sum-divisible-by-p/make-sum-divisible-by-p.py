class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0

        prefix_sums = {0: -1}
        curr_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            curr_sum += num
            target_sum = (curr_sum - remainder) % p

            if target_sum in prefix_sums:
                min_length = min(min_length, i - prefix_sums[target_sum])

            prefix_sums[curr_sum % p] = i

        return min_length if min_length < len(nums) else -1