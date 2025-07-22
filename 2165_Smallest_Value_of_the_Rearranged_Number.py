class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = num < 0
        s = str(num)
        if neg:
            s = s[1:]
        arr = sorted(s, reverse=neg)
        i = 0
        while i < len(arr) and arr[i] == '0':
            i += 1
        if 0 < i < len(arr):
            arr[i], arr[0] = arr[0], arr[i]
        s = ''.join(arr)
        if neg:
            s = '-' + s
        return int(s)