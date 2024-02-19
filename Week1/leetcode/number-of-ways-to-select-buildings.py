class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot=0
        check=[[0]*2 for i in range (2)]

        for i in range(len(s)):
            cur=int(s[i])
            tot+=check[1][1-cur]
            check[1][cur]+=check[0][1-cur]
            check[0][cur]+=1


        return tot


       
