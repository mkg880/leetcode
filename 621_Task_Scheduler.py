class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [(-c[key], key) for key in c]
        returning = []
        heapify(heap)
        t = 0
        idles = 0
        while c:
            if returning and returning[0][0] == t:
                _, task = heappop(returning)
                heappush(heap, (-c[task], task))
            if heap:
                cnt, task = heappop(heap)
                if cnt < -1:
                    heappush(returning, (t + n + 1, task))
                c[task] -= 1
                if c[task] == 0:
                    del c[task]
            else:
                idles += 1
            t += 1
        return t