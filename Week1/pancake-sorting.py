class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        a = len(A)
        b = []
        
        for i in range(a):
            max1 = max(A[:a - i])
            maxi = A.index(max1) + 1
            A[:maxi] = reversed(A[:maxi])
            b.append(maxi)
            
            A[:a - i] = reversed(A[:a - i])
            b.append(a - i)     
        return b