class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.ones = 0
        self.flipped = False

    def fix(self, idx: int):
        if self.flipped and self.bits[idx]:
            self.bits[idx] = 0
            self.ones += 1
			
        elif not self.flipped and not self.bits[idx]:
            self.bits[idx] = 1
            self.ones += 1

    def unfix(self, idx: int):
        if self.flipped and not self.bits[idx]:
            self.bits[idx] = 1
            self.ones -= 1
			
        elif not self.flipped and self.bits[idx]:
            self.bits[idx] = 0
            self.ones -= 1

    def flip(self):
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self):
        return self.ones == self.size

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        if self.flipped:
            return "".join("0" if i else "1" for i in self.bits)
        return "".join("1" if i else "0" for i in self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()