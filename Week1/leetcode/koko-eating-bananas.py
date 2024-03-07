class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s,e=1,max(piles)
        res=e

        while s<=e:
            k=(s+e)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:
                res=min(res,k)
                e=k-1
            else:
                s=k+1
        return res


