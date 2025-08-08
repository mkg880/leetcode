class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: -abs(x[1] - x[0]))
        n = len(costs) // 2
        a, b, res = 0, 0, 0
        for a_cost, b_cost in costs:
            if b == n or (a_cost < b_cost and a < n):
                a += 1
                res += a_cost
            else:
                b += 1
                res += b_cost
        return res
