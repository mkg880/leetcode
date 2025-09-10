import heapq
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        heap = []
        for i in range(26):
            c = chr(ord('a') + i)
            heap.append((m.get(c, 0), c))
        heapq.heapify(heap)
        chrs = []
        for i in range(m.get('?', 0)):
            cnt, ch = heapq.heappop(heap)
            chrs.append(ch)
            heapq.heappush(heap, (cnt+1, ch))
        chrs.sort()
        i = 0
        res = ''
        for c in s:
            if c != '?':
                res += c
            else:
                res += chrs[i]
                i += 1
        return res