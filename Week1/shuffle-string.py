class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        track={}
        res=[]

        for i in range(len(s)):
            track[indices[i]] = s[i]
       
        for i in range(len(s)):
            res.append(track[i])
        return "".join(res)



