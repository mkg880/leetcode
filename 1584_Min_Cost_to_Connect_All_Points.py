from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i, j, dist])
        
        id = list(range(n))
        def find(x):
            while id[x] != x:
                x = id[x]
            return x
        def union(x, y):
            id[find(x)] = find(y)
        
        res = 0
        cnt = 0
        edges.sort(key=lambda x: x[2])
        for x, y, w in edges:
            if cnt == n-1:
                break
            if find(x) == find(y):
                continue
            union(x, y)
            res += w
            cnt += 1
        return res