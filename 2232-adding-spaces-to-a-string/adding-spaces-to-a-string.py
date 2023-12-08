class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = ''
        prev = 0

        for space in spaces:
            ans += s[prev:space] + ' '
            prev = space
            if space == spaces[-1]:
                return ans + s[prev : ]