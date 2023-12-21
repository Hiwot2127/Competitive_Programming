class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for j in range(len(strs[0])):
            prev='A'
            for i in range(len(strs)):
                if strs[i][j]<prev:
                   count+=1
                   break
                prev=strs[i][j]
        return count


               


        