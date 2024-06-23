class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
       secrets=set([0,firstPerson])
       tmap={}
       for src,dst,t in meetings:
            if t not in tmap:
                tmap[t]=defaultdict(list)
            tmap[t][src].append(dst)
            tmap[t][dst].append(src)
       def dfs(src,adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei,adj)
       for t in sorted(tmap.keys()):
            visit=set()
            for src in tmap[t]:
                if src in secrets:
                    dfs(src,tmap[t])

       return list(secrets)