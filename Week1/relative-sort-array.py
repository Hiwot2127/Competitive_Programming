class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_dict = {val: i for i, val in enumerate(arr2)}

        def custom_sort_key(x):
            return order_dict.get(x, len(arr2) + x)

        arr1.sort(key=custom_sort_key)

        return arr1