class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        ans = 0
        for house in houses:
            i= bisect.bisect_left(heaters, house)
            dif = abs(heaters[i-1]-house)
            if i<len(heaters): dif = min(dif, abs(heaters[i]-house))
            if i+1<len(heaters): dif = min(dif, abs(heaters[i+1]-house))
            ans = max(ans, dif)
        return ans
            


       
