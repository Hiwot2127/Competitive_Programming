class Solution:
    def simplifyPath(self, path: str) -> str:

        strs = path.split('/')
        ans = []

        for s in strs:
            if s == '..':
                if ans:
                    ans.pop()

            elif s.isalpha() or (s and s!='.'):
                ans.append(s)

        return '/' + '/'.join(ans)