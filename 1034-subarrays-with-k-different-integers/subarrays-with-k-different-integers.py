class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        start = 0
        mend = 0
        miend = 0
        res = 0
        fmin = collections.defaultdict(int)
        fmax = collections.defaultdict(int)
        unique = 0

        for start in range(len(nums)):

            while miend < len(nums) and unique < k:
                if fmin[nums[miend]] == 0:
                    unique += 1
                fmin[nums[miend]] += 1
                miend += 1
            
            while mend < len(nums) and fmin[nums[mend]]:
                fmax[nums[mend]] += 1
                mend += 1
            
            if unique != k:
                break

            res += mend - miend + 1
            fmin[nums[start]] -= 1
            fmax[nums[start]] -= 1
            if fmin[nums[start]] == 0:
                unique -= 1
        
        return res

            


