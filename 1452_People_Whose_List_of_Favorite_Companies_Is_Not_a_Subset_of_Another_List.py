class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        m = {}
        for i, arr in enumerate(favoriteCompanies):
            for s in arr:
                m[s] = m.get(s, set()) | {i}
        res = []
        for i, arr in enumerate(favoriteCompanies):
            s = m[arr[0]]
            for i in range(1, len(arr)):
                s = s & m[arr[i]]
            if len(s) > 1:
                res.append(i)
        return res