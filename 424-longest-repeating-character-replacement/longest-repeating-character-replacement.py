class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         
        prev = {}
        window = 0
        
        for i, char in enumerate(s):
            prev[char] = prev.get(char, 0) + 1

            if window+1 - max(prev.values()) <= k:
                window += 1
            else:
                prev[s[i-window]] -= 1
        
        return window
        
  
