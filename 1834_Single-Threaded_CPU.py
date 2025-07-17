class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(task, i) for i, task in enumerate(tasks)])
        time = 1
        heap = []
        i = 0
        res = []
        while i < len(sorted_tasks):
            while i < len(sorted_tasks) and sorted_tasks[i][0][0] <= time:
                (enque, processing), idx = sorted_tasks[i]
                heappush(heap, (processing, idx, enque))
                i += 1
            if heap:
                processing, idx, enque = heappop(heap)
                res.append(idx)
                time += processing
            else:
                time = sorted_tasks[i][0][0]
        while heap:
            _, idx, _ = heappop(heap)
            res.append(idx)
        return res