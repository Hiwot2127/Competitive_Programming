from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N = len(nums1)
        count = 0
        sl = SortedList()
        for i in range(N):
            count += sl.bisect_right(nums1[i]-nums2[i]+diff)
            sl.add(nums1[i] - nums2[i])
        return count