class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end = 1
        ans = []
        
        while end < len(s):
            if not set(s[start:end]) & set(s[end:]):
                ans.append(len(s[start:end]))
                start = end
                end += 1
            else:
                end +=1
        else: 
            ans.append(len(s[start:end]))

        return ans
