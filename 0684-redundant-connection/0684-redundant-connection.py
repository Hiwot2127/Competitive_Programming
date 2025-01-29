class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[-1]*(len(edges)+1)
        rank=[0]*(len(edges)+1)

        def find(x):
            if parent[x]==-1:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parx=find(x)
            pary=find(y)
            if parx==pary:
                return False
            elif rank[parx]<rank[pary]:
                parent[parx]=pary
                rank[pary]+=1
                return True
            else:
                parent[pary]=parx
                rank[parx]+=1
                return True
        for a,b in edges:
            if not union(a,b):
                return[a,b]
        