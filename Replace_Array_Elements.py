class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        itoNum= {j:i for i,j in enumerate(nums)}

        for i in operations:
            nums[itoNum[i[0]]]=i[1]
            temp=itoNum[i[0]]
            itoNum.pop(i[0])
            itoNum[i[1]]=temp

        return nums
