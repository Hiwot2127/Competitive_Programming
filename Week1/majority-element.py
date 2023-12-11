class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track= Counter(nums)

        for num in nums:
             if track[num]>=(len(nums)/2):
                 return num