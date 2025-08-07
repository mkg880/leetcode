class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        id = list(range(n))
        def find(p):
            while p != id[p]:
                p = id[p]
            return p
        def union(p, q):
            id[find(p)] = find(q)

        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        comp = 0
        for i in range(n):
            if id[i] == i:
                comp += 1
        return n - comp