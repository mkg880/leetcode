class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        start = 0
        while start < n and s[start] == 'a':
            start += 1
        if start == n:
            return 'a' * (n-1) + 'z'
        end = start
        while end < n and s[end] != 'a':
            end += 1
        temp = ''.join(chr(ord(s[i]) - 1) for i in range(start, end))
        return s[:start] + temp + s[end:]