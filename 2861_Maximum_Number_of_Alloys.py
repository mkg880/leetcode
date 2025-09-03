from math import ceil
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def possible(amt):
            for arr in composition:
                total = 0
                for i in range(n):
                    needed = max(arr[i] * amt - stock[i], 0)
                    total += needed * cost[i]
                if total <= budget:
                    return True
            return False
        lo, hi = 0, budget + max(stock)
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo