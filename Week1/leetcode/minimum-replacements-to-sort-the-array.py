class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        prev=nums[-1]

        for num in reversed(nums[:-1]):
            cur=(num+prev-1)//prev
            count+=cur-1
            prev=num//cur
        return count
