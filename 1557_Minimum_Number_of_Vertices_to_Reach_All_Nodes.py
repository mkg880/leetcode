class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = set([i for i in range(n)])
        for _, b in edges:
            if b in s:
                s.remove(b)
        return list(s)