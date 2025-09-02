from collections import defaultdict
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        sorted_queries = sorted([(val, i) for i, val in enumerate(queries)])
        res = [0] * len(queries)
        i = 0
        j = 0
        m = defaultdict(int)
        used = 0
        for r, idx in sorted_queries:
            l = r - x
            while j < len(logs) and logs[j][1] <= r:
                if not m[logs[j][0]]:
                    used += 1
                m[logs[j][0]] += 1
                j += 1
            while i < len(logs) and logs[i][1] < l:
                m[logs[i][0]] -= 1
                if not m[logs[i][0]]:
                    used -= 1
                i += 1
            res[idx] = n - used
        return res