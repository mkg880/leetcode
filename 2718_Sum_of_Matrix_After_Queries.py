class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows, cols = set(), set()
        res = 0
        for type, idx, val in reversed(queries):
            if type == 0:
                if idx in rows:
                    continue
                res += val * (n - len(cols))
                rows.add(idx)
            else:
                if idx in cols:
                    continue
                res += val * (n - len(rows))
                cols.add(idx)
        return res