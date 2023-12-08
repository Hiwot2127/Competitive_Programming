class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        one=len(num1)
        two=len(num2)

        for i in range(one):
            a= 10**i
            for j in range(two):
                res+=(ord(num1[one-1-i])- ord('0'))*(ord(num2[two-1-j])-ord('0'))*a 
                a*=10
        return str(res)

        