class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        count1= Counter(nums)

        for key, value in count1.items():
            if value > 1:
                res += value*(value-1)//2
        return res


       


           
            
            
