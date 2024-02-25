class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shot=1
        points.sort(key=lambda x:x[0])
        prev=points[0][1]
        for x,y in points[1:]:
            if x<=prev:
                prev=min(y, prev)
                continue
            prev=y
            shot+=1
        return shot
