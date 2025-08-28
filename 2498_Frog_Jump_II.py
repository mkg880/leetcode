class Solution:
    def maxJump(self, stones: List[int]) -> int:
        prev_f = 0
        prev_b = 0
        res = float('-inf')
        for i in range(1, len(stones)):
            if i % 2 == 1:
                res = max(res, stones[i] - prev_b)
                prev_b = stones[i]
            else:
                res = max(res, stones[i] - prev_f)
                prev_f = stones[i]
        return res