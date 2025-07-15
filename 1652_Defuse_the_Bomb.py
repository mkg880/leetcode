class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            start = 1
            end = k
        else:
            start = len(code) + k
            end = len(code) - 1
        val = 0
        res = []
        for i in range(start, end+1):
            val += code[i]
        for i in range(len(code)):
            res.append(val)
            val -= code[start%len(code)]
            val += code[(end+1)%len(code)]
            start += 1
            end += 1
        return res