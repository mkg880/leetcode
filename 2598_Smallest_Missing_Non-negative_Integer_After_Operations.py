class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = {}
        for n in nums:
            mod = n % value
            m[mod] = m.get(mod, 0) + 1
        times = 0
        while True:
            for i in range(value):
                val = m.get(i, 0)
                if val == 0:
                    return value * times + i
                else:
                    m[i] -= 1
            times += 1