class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        m = {}
        for idx, word in enumerate(arr):
            m[idx] = set()
            n = len(word)
            for i in range(n):
                curr = ''
                for j in range(i, n):
                    curr += word[j]
                    m[idx].add(curr)
        res = []
        for idx, word in enumerate(arr):
            ans = ''
            s = set()
            for key in m:
                if key != idx:
                    s.update(m[key])
            n = len(word)
            for i in range(n):
                curr = ''
                for j in range(i, n):
                    curr += word[j]
                    if curr not in s and (not ans or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans)):
                        ans = curr
            res.append(ans)
        return res