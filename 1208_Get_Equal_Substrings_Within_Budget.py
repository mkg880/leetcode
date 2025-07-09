class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        start = 0
        curr = 0
        res = 0
        for end in range(len(s)):
            curr += arr[end]
            while curr > maxCost:
                curr -= arr[start]
                start += 1
            res = max(res, end - start + 1)
        return res