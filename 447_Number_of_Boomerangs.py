class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [[-1] * n for _ in range(n)]
        for i in range(1, n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                distance = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
                dist[i][j] = distance
                dist[j][i] = distance
        res = 0
        for i in range(n):
            arr = sorted(dist[i])
            last = arr[0]
            cnt = 1
            for j in range(n):
                if arr[j] == -1:
                    res += cnt * (cnt - 1)
                    cnt = 1
                    continue
                if arr[j] == last:
                    cnt += 1
                else:
                    res += cnt * (cnt - 1)
                    cnt = 1
                    last = arr[j]
            res += cnt * (cnt - 1)
        return res