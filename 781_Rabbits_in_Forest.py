class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        res = 0
        for key in c:
            add = c[key]
            rem = c[key] % (key+1)
            if rem:
                add += key + 1 - rem
            res += add
        return res