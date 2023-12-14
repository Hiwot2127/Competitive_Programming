class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        left_count, left_sum = 0, 0

        for i in range(n):
            res[i] += left_sum
            left_count += int(boxes[i])
            left_sum += left_count

        right_count, right_sum = 0, 0

        for i in range(n - 1, -1, -1):
            res[i] += right_sum
            right_count += int(boxes[i])
            right_sum += right_count

        return res
