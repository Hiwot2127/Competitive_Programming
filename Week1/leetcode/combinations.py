class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]

        def back(start,cur):
            if len(cur)==k:
                ans.append(cur.copy())
                return

            for i in range(start, n+1):
                cur.append(i)
                back(i+1,cur)
                cur.pop()

        back(1,[])
        return ans