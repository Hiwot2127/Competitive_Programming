class CustomStack:

    def __init__(self, maxSize: int):
        self.nums=[]
        self.maxi=maxSize

    def push(self, x: int) -> None:
        if len(self.nums)<self.maxi:
            self.nums.append(x)

    def pop(self) -> int:
        if len(self.nums)==0:
            return -1
        else:
            return self.nums.pop()

    def increment(self, k: int, val: int) -> None:
        if k<=len(self.nums):
            for i in range(k):
                self.nums[i]+=val
        else:
            for i in range(len(self.nums)):
                self.nums[i]+=val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)