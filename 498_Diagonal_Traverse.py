class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in m:
                    m[i+j] = []
                m[i+j].append(mat[i][j])
        res = []
        idx = 0
        while idx in m:
            if idx % 2 == 0:
                m[idx].reverse()
            for val in m[idx]:
                res.append(val)
            idx += 1
        return res