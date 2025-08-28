class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pen = [0] * (n+1)
        nos = 0
        for i in range(n+1):
            pen[i] += nos
            nos += 1 if i < n and customers[i] == 'N' else 0
        yes = 0
        for i in range(n, -1, -1):
            yes += 1 if i < n and customers[i] == 'Y' else 0
            pen[i] += yes
        min_pen, idx = float('inf'), -1
        for i in range(n+1):
            if pen[i] < min_pen:
                min_pen = pen[i]
                idx = i
        return idx