class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis=[float("inf")]*n
        dis[src]=0

        for i in range(k+1):
            temp=dis[:]
            for u,v,p in flights:
                if dis[u]!=float("inf"):
                    temp[v]=min(temp[v],dis[u]+p)
            dis=temp
        return dis[dst] if dis[dst]!=float("inf") else -1

