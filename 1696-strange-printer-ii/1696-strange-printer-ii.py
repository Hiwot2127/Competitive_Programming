class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n, dict1 = len(targetGrid), len(targetGrid[0]), defaultdict(set)

        for c in range(1,61):
            i_mn = j_mn = 60
            i_mx = j_mx = 0

            for i in range(m):
                for j in range(n):
                    if targetGrid[i][j] == c:
                        i_mn = min(i_mn,i)
                        i_mx = max(i_mx,i)
                        j_mn = min(j_mn,j)
                        j_mx = max(j_mx,j)

            for i in range(i_mn,i_mx+1):
                for j in range(j_mn,j_mx+1):
                    if targetGrid[i][j] != c:
                        dict1[c].add(targetGrid[i][j])

        def dfs(n):
            if visited[n]: return visited[n] == 1
            visited[n] = 1
            if any(dfs(j) for j in dict1[n]): return True
            visited[n] = 2
            return False 

        visited = [0]*61

        return not any(dfs(i) for i in range(61))