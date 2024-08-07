class Solution:
    def countArrangement(self, n: int) -> int:
        self.h = 0
        nums = [i for i in range(1, n+1)]

        def dfs (nums, i = 1):
            if i == n+1:
                self.h +=1
                return
            for j, num in enumerate(nums):
                if not (num % i and i% num):
                    dfs(nums[:j] + nums[j+1:], i+1)
        dfs(nums)
        return self.h