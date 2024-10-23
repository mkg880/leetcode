class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for s in strs:
            arr = str(sorted(list(s)))
            if arr not in D:
                D[arr] = []
            D[arr].append(s)
        res = []
        for i in D:
            res.append(D[i])
        return res
