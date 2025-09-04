import heapq
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        arr = [1] * n
        for i in range(1, n):
            if s[i] == s[i-1]:
                arr[i] = arr[i-1] + 1
        m = {}
        for i in range(n):
            if s[i] not in m:
                m[s[i]] = []
            if len(m[s[i]]) == 3 and m[s[i]][0] < arr[i]:
                heapq.heappop(m[s[i]])
            if len(m[s[i]]) < 3:
                heapq.heappush(m[s[i]], arr[i])
        return max(heap[0] if len(heap) == 3 else -1 for heap in m.values())