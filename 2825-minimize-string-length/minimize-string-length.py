class Solution:
    def minimizedStringLength(self, s: str) -> int:
       track=set(s)
       return len(track)