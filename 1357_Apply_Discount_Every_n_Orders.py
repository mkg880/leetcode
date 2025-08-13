class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.discount = n, discount
        self.price = {}
        for product, price in zip(products, prices):
            self.price[product] = price
        self.cnt = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        discount = self.cnt % self.n == 0
        res = 0
        for p, a in zip(product, amount):
            res += self.price[p] * a
        if discount:
            res = res * ((100 - self.discount) / 100)
        return res



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)