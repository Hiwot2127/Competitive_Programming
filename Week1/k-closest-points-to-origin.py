class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            dis = pow((pow((0 - point[0]), 2) + pow((0 - point[1]), 2)), 0.5)
            distance.append([point, dis])

        distance.sort(key=lambda x: x[1])
        result = []
        for i in range(k):
            result.append(distance[i][0])
        return result