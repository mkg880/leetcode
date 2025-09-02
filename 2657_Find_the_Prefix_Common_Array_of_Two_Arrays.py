class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        m = set()
        n = len(A)
        cnt = 0
        res = []
        for i in range(n):
            if A[i] in m:
                cnt += 1
            m.add(A[i])
            if B[i] in m:
                cnt += 1
            m.add(B[i])
            res.append(cnt)
        return res