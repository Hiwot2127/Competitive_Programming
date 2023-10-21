class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts=[0]*3
        
        for i in nums:
            counts[i]+=1
        i=0
        for j in range(3):
            while counts[j]>0:
                nums[i]=j
                i+=1
                counts[j]-=1
        
