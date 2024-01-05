class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(target - current_sum)

                if current_diff < min_diff:
                    closest_sum = current_sum
                    min_diff = current_diff

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
    