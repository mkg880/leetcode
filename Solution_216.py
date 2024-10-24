class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def rec(i, arr, total):
            if len(arr) == k and total == n:
                res.append(arr)
            elif len(arr) < k:
                for idx in range(i, 10):
                    val = total + idx
                    if val <= n and idx not in arr:
                        rec(idx, arr + [idx], val)
        rec(1, [], 0)
        return res