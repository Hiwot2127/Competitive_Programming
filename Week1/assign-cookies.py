class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j=0,0
        s.sort()
        g.sort()
        res=0

        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                res+=1
                j+=1
                i+=1
            else:
                i+=1
        return res