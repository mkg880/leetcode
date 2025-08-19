class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        curr = 0
        pre = [0] * n
        post = [0] * n
        for i in range(n):
            pre[i] = curr
            if s[i] == 'b':
                curr += 1
        curr = 0
        for i in range(n-1, -1, -1):
            post[i] = curr
            if s[i] == 'a':
                curr += 1
        return min(pre[i] + post[i] for i in range(n))