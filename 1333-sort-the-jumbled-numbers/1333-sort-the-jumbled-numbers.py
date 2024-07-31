class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = {}
        for num in nums:
            if num in mapped: 
                continue
            mapped[num] = int(''.join(str(mapping[int(d)]) for d in str(num)))

        return sorted(nums, key = mapped.get)