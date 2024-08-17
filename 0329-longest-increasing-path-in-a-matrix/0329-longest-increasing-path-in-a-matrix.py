class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        vis = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j):
            if vis[i][j] > 0:
                return vis[i][j]
            vis[i][j] = 1
            res = 0
            row = [1, -1, 0, 0]
            col = [0, 0, 1, -1]
            for k in range(4):
                r, c = i + row[k], j + col[k]
                if r >=0 and r < m and c >= 0 and c < n:
                    if matrix[r][c] > matrix[i][j]:
                        res = max(res, dfs(r, c))
            vis[i][j] += res
            return vis[i][j]
        ret = 0
        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret