class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box= set()
        left=0
        ans=0

        for right in range(len(s)):

            while s[right] in box:
                box.remove(s[left])
                left+=1
            box.add(s[right])
            ans= max(ans, right-left+1)

        return ans


