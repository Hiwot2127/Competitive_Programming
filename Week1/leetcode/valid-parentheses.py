class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isMatching(opening, closing):
            return (opening == '(' and closing == ')') or (opening == '{' and closing == '}') or (opening == '[' and closing == ']')
                
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack or not isMatching(stack[-1], char):
                    return False
                stack.pop()
        return len(stack) == 0

  