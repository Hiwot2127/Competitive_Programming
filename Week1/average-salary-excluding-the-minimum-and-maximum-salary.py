class Solution:
    def average(self, salary: List[int]) -> float:
        org=sorted(salary)
        n=len(org)
        avg=0
        sum1=sum(org)
        
        sum1-= (org[0]+org[-1])
        avg=sum1/(n-2)
        return avg



        