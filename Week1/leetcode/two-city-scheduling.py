class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dif=[]
        for a,b in costs:
            dif.append([b-a, a, b])
        dif.sort()
        ans=0
        for i in range(len(dif)):
            if i<len(dif)//2:
                ans+=dif[i][2]
            else:
                ans+=dif[i][1]
        return ans
            
        