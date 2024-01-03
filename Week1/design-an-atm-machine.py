class ATM:
    def __init__(self):
        self.money = [0, 0, 0, 0, 0]
        self.order = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, amount in enumerate(banknotesCount):
            self.money[i] += amount

    def withdraw(self, amount: int) -> List[int]:
        output = [0,0,0,0,0] 
        i = 4
        while amount and i >= 0:
            output[i] = min(self.money[i], amount // self.order[i])
            amount -= output[i] * self.order[i]
            i -= 1

        if amount:
            return [-1]
        else:
            for i, mon in enumerate(self.money):
                self.money[i] = mon - output[i]
            return output


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
