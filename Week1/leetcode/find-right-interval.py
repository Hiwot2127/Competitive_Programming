class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        track={}
        for i, interval in enumerate(intervals):
            track[interval[0]]=i
        sintervals=sorted(intervals, key=lambda x:x[0])
        res=[-1]*len(intervals)

        for i, interval in enumerate(intervals):
            index=bisect_left(sintervals,[interval[1],-float('inf')])
            if index!=len(intervals):
                res[i]=track[sintervals[index][0]]
        return res
