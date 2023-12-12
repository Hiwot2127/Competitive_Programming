class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        track= Counter(nums)
        res=set()

        for num in nums:
            if track[num]>(len(nums)/3):
                res.add(num)
        return res
