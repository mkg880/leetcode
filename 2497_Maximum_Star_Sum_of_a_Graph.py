import heapq
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k == 0:
            return max(vals)
        n = len(vals)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            if len(graph[a]) == k and graph[a][0] < vals[b]:
                heapq.heappop(graph[a])
            if len(graph[a]) < k and vals[b] > 0:
                heapq.heappush(graph[a], vals[b])
            if len(graph[b]) == k and graph[b][0] < vals[a]:
                heapq.heappop(graph[b])
            if len(graph[b]) < k and vals[a] > 0:
                heapq.heappush(graph[b], vals[a])
        return max(sum(graph[i]) + vals[i] for i in range(n))