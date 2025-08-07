class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            start, end = i, i
            while start >=0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            if end - start - 1 > len(res):
                res = s[start+1:end]
        for i in range(n-1):
            if s[i] != s[i+1]:
                continue
            start, end = i, i+1
            while start >=0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            if end - start - 1 > len(res):
                res = s[start+1:end]
        return res