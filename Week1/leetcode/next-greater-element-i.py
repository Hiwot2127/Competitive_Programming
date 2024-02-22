class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans= defaultdict(lambda: -1)
        for num in nums2:
            while stack and stack[-1]<num:
                ans[stack[-1]]=num
                stack.pop()
            stack.append(num)
        return [ans[num] for num in nums1]