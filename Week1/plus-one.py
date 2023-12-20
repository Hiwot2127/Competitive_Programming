class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
              strs = list(map(str, digits))
              strs1="".join(strs)
              int1=int(strs1)
              res=int1+1
              res1=str(res)
              ans=list(res1)
              ans1=list(map(int, ans))
              return ans1

               