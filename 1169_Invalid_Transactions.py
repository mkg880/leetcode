class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        names = []
        times = []
        amounts = []
        cities = []
        for s in transactions:
            n, t, a, c = s.split(",")
            names.append(n)
            times.append(int(t))
            amounts.append(int(a))
            cities.append(c)
        res = []
        for i in range(len(transactions)):
            b = False
            if amounts[i] > 1000:
                b = True
            else:
                for j in range(len(transactions)):
                    if abs(times[i] - times[j]) <= 60 and names[i] == names[j] and cities[i] != cities[j]:
                        b = True
                        break
            if b:
                res.append(transactions[i])
        return res