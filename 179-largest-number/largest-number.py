class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            xy = str(x) + str(y)
            yx = str(y) + str(x)

            return (xy > yx) - (xy < yx)

        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare), reverse=True)
        result = ''.join(nums_str)                           
        result = str(int(result))

        return result