class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {}
        for i in range(n):
            x1, y1, r = bombs[i]
            graph[i] = []
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2:
                    graph[i].append(j)
        res = 0
        for i in range(n):
            stack = [i]
            vis = set()
            cnt = 0
            while stack:
                curr = stack.pop()
                if curr in vis:
                    continue
                vis.add(curr)
                cnt += 1
                for neighbor in graph[curr]:
                    stack.append(neighbor)
            res = max(res, cnt)
        return res