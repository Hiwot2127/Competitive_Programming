class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        count=0
        flag=0

        for i in range(len(s)):
            if s[i]=="(":
                flag=1
                stack.append("(")
            if s[i]==")":
                if flag==1:
                    count+= 2**(len(stack)-1)
                    flag=0
                stack.pop()
        return count
            

        