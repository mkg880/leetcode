from heapq import heappop, heappush
class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        n = len(s)
        m = {}
        to_remove = set()
        for i in range(n):
            if s[i] == '*':
                c = heappop(heap)
                idx = m[c].pop()
                to_remove.add(i)
                to_remove.add(idx)
            else:
                heappush(heap, s[i])
                if s[i] not in m:
                    m[s[i]] = []
                m[s[i]].append(i)
        res = ''
        for i in range(n):
            if i not in to_remove:
                res += s[i]
        return res