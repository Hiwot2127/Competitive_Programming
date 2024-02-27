class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def count(x,n):
            if n==0:
                return 1
            res=count(x,n//2)
            res=res*res
            return x*res % (10**9+7) if n%2 else res % (10**9+7)
        if n==1:
            return 5
        if n%2==0:
            res=count(5, n//2)*count(4,n//2)
        else:
            res=count(5, ceil(n/2))*count(4, n//2)
        return (res % (10**9+7))
