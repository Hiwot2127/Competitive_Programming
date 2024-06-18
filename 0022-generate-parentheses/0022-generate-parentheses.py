class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def back(open,close):
            if open==close==n:
                res.append("".join(stack))
                return
            if open<n:
                stack.append('(')
                back(open+1,close)
                stack.pop()
            if close<open:
                stack.append(')')
                back(open,close+1)
                stack.pop()
        back(0,0)
        return res