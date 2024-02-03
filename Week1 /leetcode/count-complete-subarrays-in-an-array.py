class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        k = len(set(nums))
        left, count = 0, 0
        total_sub_arrays = (n * (n + 1)) // 2

        for right in range(len(nums)):
            d[nums[right]] += 1
            
            while len(d) == k:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1

            count += right - left + 1

        return total_sub_arrays - count