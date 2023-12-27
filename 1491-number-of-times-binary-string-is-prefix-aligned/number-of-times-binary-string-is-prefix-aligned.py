class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        left=0
        track=[0 for i in range(len(flips))]

        for i in range( len(flips)):
            if left<flips[i]:
                left=flips[i]
            if left==i+1:
                count+=1
        return count   

        


