class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for start, end, d in shifts:
            if d == 0:
                d = -1
            arr[start] += d
            arr[end+1] += d * -1
        pre = 0
        res = ''
        for i in range(len(s)):
            pre += arr[i]
            val = (ord(s[i]) - ord('a') + pre + 26) % 26 + ord('a')
            res += chr(val)
        return res