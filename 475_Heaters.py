class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def closest(target):
            res = heaters[0]
            lo = 0
            hi = len(heaters) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if abs(heaters[mid] - target) < abs(res - target):
                    res = heaters[mid]
                elif abs(heaters[mid] - target) == abs(res - target):
                    res = max(res, heaters[mid])
                if heaters[mid] == target:
                    return heaters[mid]
                elif heaters[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return res
        res = 0
        for h in houses:
            c = closest(h)
            res = max(res, abs(c-h))
        return res