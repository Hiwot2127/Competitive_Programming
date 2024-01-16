class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
         self.matrix = matrix
         self.sMatrix = matrix

         for i in range(len(matrix)):
             for j in range(1,len(matrix[0])):
                 self.sMatrix[i][j]+=self.sMatrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        i = row1
        j= col1
        sums=0

        while(i<=row2):
            if(col1-1>=0):
                sums+=(self.sMatrix[i][col2] - self.sMatrix[i][col1-1])
            else:
                sums+=self.sMatrix[i][col2]
            i+=1
        return sums
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)