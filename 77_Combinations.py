class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def rec(arr, idx):
            if len(arr) == k:
                res.append(arr)
                return
            for i in range(idx, n+1):
                rec(arr + [i], i+1)
        rec([], 1)
        return res