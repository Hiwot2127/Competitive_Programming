class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_integers = []
        negative_integers = []

        for num in nums:
            if num > 0:
                positive_integers.append(num)
            else:
                negative_integers.append(num)

        result = []

        for i in range(len(positive_integers)):
            result.append(positive_integers[i])
            result.append(negative_integers[i])
            
        if len(positive_integers) > len(negative_integers):
            result.append(positive_integers[-1])
        elif len(negative_integers) > len(positive_integers):
            result.append(negative_integers[-1])

        return result