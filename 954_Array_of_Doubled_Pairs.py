class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda x: abs(x))
        c = Counter(arr)
        n = len(arr)
        for val in arr:
            if c[val] == 0:
                continue
            double = val * 2
            if c[double] == 0:
                return False
            c[double] -= 1
            c[val] -= 1
        return True