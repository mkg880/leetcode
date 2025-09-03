class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for _, b in edges:
            indeg[b] += 1
        res = None
        for i in range(n):
            if indeg[i] == 0:
                if res is None:
                    res = i
                else:
                    return -1
        return res