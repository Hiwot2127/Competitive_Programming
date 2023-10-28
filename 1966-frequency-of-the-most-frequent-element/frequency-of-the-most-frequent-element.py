class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right= 0, 0
        ans, total=0, 0

        while right < len(nums):
            total+=nums[right]

            while nums[right]*(right - left +1)>total+k:
                total-=nums[left]
                left+=1
            ans= max(ans, right-left+1)
            right+=1
        return ans



        