class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        observed = sum(rolls)
        total = mean * (n + m)
        rem = total - observed
        avg = rem / n
        if not 1 <= avg <= 6:
            return []
        val = int(avg)
        mod = rem % n
        res = [val] * n
        for i in range(mod):
            res[i] += 1
        return res