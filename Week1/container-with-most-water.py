class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            ans = max(area,ans)
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
                
        return ans