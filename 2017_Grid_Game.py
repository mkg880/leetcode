class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top, bottom = grid
        n = len(top)
        pre = [0] * n
        post = [0] * n
        curr = 0
        for i in range(n):
            curr += top[i]
            pre[i] = curr
        curr = 0
        for i in range(n-1, -1, -1):
            curr += bottom[i]
            post[i] = curr
        top_total = pre[-1]
        bottom_total = post[0]
        min_val = float('inf')
        for i, (t, b) in enumerate(zip(pre, post)):
            val = max(top_total - pre[i], bottom_total - post[i])
            min_val = min(min_val, val)
        return min_val