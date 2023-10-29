class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d= {0: 1}
        count=0
        sum1=0

        for num in nums:
            sum1+=num
            diff=sum1-k

            if diff in d:
                count+=d[diff]
            if sum1 in d:
                d[sum1]+=1
            else:
                d[sum1]=1
        return count

