class ATM:

    def __init__(self):
        self.cnts = [0] * 5
        self.order = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.cnts[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        curr = amount
        for i in range(4, -1, -1):
            if not self.cnts[i] or self.order[i] > curr:
                continue
            x = min(curr // self.order[i], self.cnts[i])
            res[i] = x
            curr -= self.order[i] * x
        if curr:
            return [-1]
        for i in range(5):
            self.cnts[i] -= res[i]
        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)