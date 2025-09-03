class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        i = 3
        res = 0
        for t in sorted(processorTime, reverse=True):
            res = max(res, t+tasks[i])
            i += 4
        return res