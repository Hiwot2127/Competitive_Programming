class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = 0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[n], arr1[j] = arr1[j], arr1[n]
                    n += 1
        arr1[n:] = sorted(arr1[n:])
        return arr1