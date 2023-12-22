class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]

        for i in range(len(matrix[0])):
            res=[]
            for j in range(len(matrix)):
                res.append(matrix[j][i])
            ans.append(res)
        return ans
       

