class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        prev=self.generate(numRows-1)
        prevr=prev[-1]
        curr=[1]
        for i in range(1,numRows-1):
            curr.append(prevr[i-1]+prevr[i])
        curr.append(1)
        prev.append(curr)
        return prev