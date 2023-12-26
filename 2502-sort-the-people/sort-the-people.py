class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            while i > 0 and heights[i-1] < heights[i]:
                names[i-1], names[i] = names[i], names[i-1]
                heights[i-1], heights[i] = heights[i], heights[i-1]
                i -= 1
        return names