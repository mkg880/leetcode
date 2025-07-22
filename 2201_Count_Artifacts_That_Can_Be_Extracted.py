class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        s = set([(x, y) for x, y in dig])
        res = 0
        for r1, c1, r2, c2 in artifacts:
            invalid = False
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if (i, j) not in s:
                        invalid = True
                        break
                if invalid:
                    break
            if invalid:
                continue
            else:
                res += 1
        return res