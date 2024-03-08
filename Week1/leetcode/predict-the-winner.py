class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def check(left, right):
            if left > right:
                return 0
            left_choice = nums[left] - check(left + 1, right)
            right_choice = nums[right] - check(left, right - 1)
            return  max(left_choice, right_choice)
        ans = check(0,len(nums)-1)
        return True if ans >= 0 else False
           