class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        left=0
        output = 0
        
        for right, curr in enumerate(s):
            
            if curr in track:
                left = max(left, track[curr] + 1)
            output = max(output, right - left + 1)
            track[curr] = right

        return output
