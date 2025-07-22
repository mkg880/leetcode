class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        m = Counter(changed)
        changed.sort()
        res = []
        for val in changed:
            if m[val] == 0:
                continue
            double = val * 2
            m[val] -= 1
            if double not in m or m[double] <= 0:
                return []
            m[double] -= 1
            res.append(val)
        return res