class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        rowcol=[0]*row
        colcol=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    rowcol[i]+=1
                    colcol[j]+=1
        res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and (rowcol[i] > 1 or colcol[j] > 1):
                    res += 1
        return res