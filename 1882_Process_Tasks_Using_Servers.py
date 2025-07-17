class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        available = [(w, i) for i, w in enumerate(servers)]
        heapify(available)
        unavailable = []
        t = 0
        i = 0
        while i < len(tasks):
            task = tasks[i]
            t = max(t, i)
            while unavailable and unavailable[0][0] == t:
                _, idx = heappop(unavailable)
                heappush(available, (servers[idx], idx))
            if available:
                w, idx = heappop(available)
                heappush(unavailable, [t + task, idx])
                res.append(idx)
                i += 1
            else:
                t = unavailable[0][0]
        return res