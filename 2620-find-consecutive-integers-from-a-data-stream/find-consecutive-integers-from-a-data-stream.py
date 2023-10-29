class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.queue = []
        self.track = collections.defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.track[num] += 1

        if len(self.queue) > self.k:
            rmv = self.queue.pop(0)
            self.track[rmv] -= 1

        return self.track[self.val] == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)