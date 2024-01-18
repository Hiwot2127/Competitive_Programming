class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def getNextIndex(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i

            while nums[fast] * nums[i] > 0 and nums[getNextIndex(fast)] * nums[i] > 0:
                slow = getNextIndex(slow)
                fast = getNextIndex(getNextIndex(fast))

                if slow == fast:
                    if slow == getNextIndex(slow):
                        break
                    return True

            slow = i
            while nums[slow] * nums[i] > 0:
                next_slow = getNextIndex(slow)
                nums[slow] = 0
                slow = next_slow

        return False