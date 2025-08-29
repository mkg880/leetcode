class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        cnt = 0
        res = []
        for val in word:
            cnt = (cnt * 10 + int(val)) % m
            if cnt == 0:
                res.append(1)
            else:
                res.append(0)
        return res