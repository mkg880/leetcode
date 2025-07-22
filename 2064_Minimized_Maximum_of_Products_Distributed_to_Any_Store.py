class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        def can_dist(k):
            needed = 0
            for q in quantities:
                needed += ceil(q / k)
                if needed > n:
                    return False
            return True
        l, r = 1, max(quantities)
        while l < r:
            mid = (l + r) // 2
            if can_dist(mid):
                r = mid
            else:
                l = mid + 1
        return l