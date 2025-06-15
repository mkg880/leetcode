class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for a, b, c in flights:
            graph[a].append((b, c))
        x = k + 1
        min_cost = {i: float('inf') for i in range(n)}
        q = deque([(src, 0)])
        cnt = 0
        while q and cnt < x:
            current_size = len(q)
            for i in range(current_size):
                node, cost = q.popleft()
                for n, w in graph[node]:
                    if cost + w >= min_cost[n]:
                        continue
                    min_cost[n] = cost + w
                    q.append((n, min_cost[n]))
            cnt += 1
        res = min_cost[dst]
        return -1 if res == float('inf') else res