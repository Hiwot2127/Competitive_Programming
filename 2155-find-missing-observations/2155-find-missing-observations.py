class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumOfN = mean * (n + len(rolls)) - sum(rolls)
        if n > sumOfN or sumOfN > n * 6:
            return []
        answer = []
        elementsToFill = n
        
        while elementsToFill > 0:
            newElement = sumOfN // elementsToFill
            answer.append(newElement)
            elementsToFill -= 1
            sumOfN -= newElement
        
        return answer