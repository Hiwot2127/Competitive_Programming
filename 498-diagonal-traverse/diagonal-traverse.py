class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            if d % 2 == 0:
                i, j = min(d, m - 1), max(0, d - m + 1)
                while i >= 0 and j < n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                i, j = max(0, d - n + 1), min(d, n - 1)
                while i < m and j >= 0:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1

        return result