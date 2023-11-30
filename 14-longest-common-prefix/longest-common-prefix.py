class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        new=sorted(strs)
        first=new[0]
        last=new[-1]
        
        for i in range(min(len(first), len(last))):
            if(first[i]!=last[i]):
                return res
            res+=first[i]
        return res 