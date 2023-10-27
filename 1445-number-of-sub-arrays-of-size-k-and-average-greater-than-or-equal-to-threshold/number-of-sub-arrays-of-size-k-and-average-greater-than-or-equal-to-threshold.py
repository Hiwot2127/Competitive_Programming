class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        res=0
        csum=0
        
        for right in range(len(arr)):

            if right-left+1>k:
                csum-=arr[left]
                left+=1
            csum+=arr[right]

            if ((right-left+1)==k) and (csum/k)>=threshold:
                res+=1
            
        return res
