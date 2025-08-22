from collections import deque


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        curr = 0
        vis = set()
        comp_cnt = []
        for i in range(n):
            if i in vis:
                continue
            q = deque([i])
            while q:
                node = q.popleft()
                if node in vis:
                    continue
                vis.add(node)
                if curr == len(comp_cnt):
                    comp_cnt.append(0)
                comp_cnt[curr] += 1
                for neighbor in graph[node]:
                    q.append(neighbor)
            curr += 1
        return sum(val * (n-val) for val in comp_cnt) // 2