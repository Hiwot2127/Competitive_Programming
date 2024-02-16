class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1

        counts = list(freq.values())
        counts.sort()

        unique_count = len(counts)

        for count in counts:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        return unique_count