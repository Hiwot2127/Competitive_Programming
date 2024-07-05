class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis = set()
        for num in nums:
            if num in vis:
                return num
            vis.add(num)