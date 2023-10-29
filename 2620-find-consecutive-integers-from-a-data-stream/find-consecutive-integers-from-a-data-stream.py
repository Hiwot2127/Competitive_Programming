class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.curr = -1
        self.last = -1

    def consec(self, num: int) -> bool:
        self.curr += 1

        if num != self.value:
            self.last = self.curr
            
        return self.curr - self.last >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)