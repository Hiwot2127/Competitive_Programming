class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix=[0]*(1001)

        for num,i,j in trips:
            prefix[i]+=num
            prefix[j]-=num

        for i in range(1,1001):
            prefix[i]+=prefix[i-1]

        for i in range(1001):
            if prefix[i]>capacity:
                return False
        return True
        
