class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]

        res = []

        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])

        return res