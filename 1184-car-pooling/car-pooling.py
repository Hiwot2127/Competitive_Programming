class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stop = [0]*(1001)
        
        for i in trips:
            stop[i[1]]+=i[0]
            stop[i[2]]-=i[0]
            
        if stop[0] > capacity:
           return False

        for j in range(1, len(stop)):
            stop[j] += stop[j-1]
            
            if stop[j]>capacity:
                return False
                
        return True