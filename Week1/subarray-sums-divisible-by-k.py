class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = 0
        sums = {0: 1}
        count = 0

        for num in A:
            prefix += num
            key = prefix%K

            if key in sums:
                count += sums[key]
                sums[key] += 1
                continue
            sums[key] = 1

        return count