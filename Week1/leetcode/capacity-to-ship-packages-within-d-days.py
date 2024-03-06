class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weights,days,mid):
            count=1
            cur=0
            for weight in weights:
                cur+=weight
                if cur>mid:
                    count+=1
                    cur=weight
            if count>days:
                return False
            return True

        low=max(weights)
        high=sum(weights)

        while low<=high:
            mid=(low+high)//2
            if check(weights,days,mid):
                high=mid-1
            else:
                low=mid+1
        return low
            


