class Solution:
    def evalRPN(self, t: List[str]) -> int:
        b = ['+', '-', '*', '/']
        s = []

        for i in t:
            if i not in b:
                s.append(int(i))
            else:
                k, c = s.pop(), s.pop()
                if i == '+':
                    s.append(c + k)
                elif i == '-':
                    s.append(c - k)
                elif i == '*':
                    s.append(c * k)
                else:
                    s.append(int(c / k))

        return s[0]