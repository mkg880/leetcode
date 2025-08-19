class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        mod = 10 ** 9 + 7
        for i in range(22):
            p = 2 ** i
            m = {}
            for val in deliciousness:
                res = (res + m.get(p-val, 0)) % mod
                m[val] = m.get(val, 0) + 1
        return res