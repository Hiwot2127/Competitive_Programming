class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]*(rowIndex+1)
        if rowIndex==0:
            return row
        prev=self.getRow(rowIndex-1)
        for i in range(1,len(row)-1):
            row[i]=prev[i-1]+prev[i]
        return row