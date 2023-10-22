class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))
        
        if high**2 == c:
            return True
        
        while low<=high:
            x = low **2 + high **2

            if x == c:
                return True
            if x > c:
                high-=1
            else:
                low+=1
                
        return False
