class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op1,op2=0,0
        for tok in tokens:
            if tok=='+':
                if stack:
                    op1=stack.pop()
                    op2=stack.pop()
                stack.append(op1+op2)
            elif tok=='-':
                if stack:
                    op1=stack.pop()
                    op2=stack.pop()
                stack.append(op2-op1)
            
            elif tok=='*':
                if stack:
                    op1=stack.pop()
                    op2=stack.pop()
                stack.append(op1*op2)
            elif tok=='/':
                if stack:
                    op1=stack.pop()
                    op2=stack.pop()
                if op1!=0:
                    stack.append(int(op2/op1))
                else: 
                    continue
            else:
                stack.append(int(tok))
        return stack[0]
        
                
                    