class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            minChar = s[0]
            cnt = 1
            for i in range(1, len(s)):
                if s[i] < minChar:
                    minChar = s[i]
                    cnt = 1
                elif s[i] == minChar:
                    cnt += 1
            return cnt
        arr = [f(w) for w in words]
        arr.sort()
        n = len(arr)
        return [n - bisect_right(arr, f(s)) for s in queries]