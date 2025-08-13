from heapq import heappop, heappush
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        def possible(x):
            i = 0
            cnt = 0
            while i < n:
                j = i
                while j < min(n, i+k) and bloomDay[j] <= x:
                    j += 1
                if j == i+k:
                    cnt += 1
                i = j+1
            return cnt >= m
        lo, hi = 0, max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo