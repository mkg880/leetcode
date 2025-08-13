class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr, i = 1, 0
        res = []
        while i < len(target) and curr <= n:
            res.append("Push")
            if target[i] != curr:
                res.append("Pop")
            else:
                i += 1
            curr += 1
        return res