class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for f, b in zip(fronts, backs):
            if f == b:
                same.add(f)
        res = float('inf')
        for x in fronts + backs:
            if x not in same:
                res = min(res, x)
        return res if res < float('inf') else 0