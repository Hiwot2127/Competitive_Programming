class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def check(nums,target,isleft):
            cur=-1
            left,right=0, len(nums)-1

            while left<=right:
                mid=(left+right)//2
                if target<nums[mid]:
                    right=mid-1
                elif target>nums[mid]:
                    left=mid+1
                else:
                    cur=mid
                    if isleft:
                        right=mid-1
                    else:
                        left=mid+1
            return cur
        left=check(nums,target,True)
        right=check(nums,target,False)
        return [left,right]


       