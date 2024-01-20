class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        result = [0] * n
        for i in range(n):
            left_sum = nums[i] * i - (prefix_sum[i - 1] if i > 0 else 0)
            right_sum = (suffix_sum[i + 1] if i < n - 1 else 0) - nums[i] * (n - i - 1)
            result[i] = left_sum + right_sum

        return result