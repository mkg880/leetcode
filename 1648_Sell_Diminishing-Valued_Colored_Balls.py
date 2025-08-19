class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def solve(k):
            taken = 0
            for x in inventory:
                taken += max(x-k, 0)
            return taken
        lo, hi = 0, max(inventory)
        t = 0
        while lo < hi:
            mid = (lo + hi) // 2
            val = solve(mid)
            if val <= orders:
                hi = mid
                t = val
            else:
                lo = mid+1
        res = (orders - t) * lo
        mod = 10 ** 9 + 7
        for x in inventory:
            if x > lo:
                res = (res + (x-lo) * (x+lo+1) // 2) % mod
        return res