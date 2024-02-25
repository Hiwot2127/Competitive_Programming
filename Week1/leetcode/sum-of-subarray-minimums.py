class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        arr = [float('-inf')] + arr + [float('-inf')]

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                ans += arr[cur] * (i - cur)*  (cur - stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)

