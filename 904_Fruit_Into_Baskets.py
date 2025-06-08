class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        m = {}
        res = 0
        while r < len(fruits):
            if fruits[r] not in m:
                m[fruits[r]] = 0
            m[fruits[r]] += 1
            while len(m) > 2:
                m[fruits[l]] -= 1
                if m[fruits[l]] == 0:
                    del m[fruits[l]]
                l += 1
            r += 1
            res = max(res, r-l)
        return res