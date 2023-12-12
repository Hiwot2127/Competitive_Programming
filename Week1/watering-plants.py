class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 1
        capacity1 = capacity

        for i in range(len(plants)-1):
            if capacity >= plants[i]:
                res += 1
                capacity -= plants[i]
                if capacity < plants[i+1]:
                    res += i+1
                    capacity = capacity1
                    res += i+1
            
        return res

      

