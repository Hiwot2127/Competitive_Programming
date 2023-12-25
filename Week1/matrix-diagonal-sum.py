class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
            y=len(mat)
            res=0

            for i in range(y):
                res+=mat[i][i]

            for i in range(y):
                if i!=y-1-i:
                     res+=mat[i][y-1-i]
            return res

