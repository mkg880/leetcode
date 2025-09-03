class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        end = 0
        n = len(s)
        res = ''
        curr = 0
        for start in range(n):
            while end < n and curr < k:
                if s[end] == '1': curr += 1
                end += 1
            if curr < k:
                return res
            temp = s[start:end]
            if not res or len(temp) < len(res) or (len(temp) == len(res) and temp < res):
                res = temp
            if s[start] == '1': curr -= 1
        return res