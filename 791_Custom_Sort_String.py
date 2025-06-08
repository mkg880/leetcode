class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idx = {}
        for i in range(len(order)):
            idx[order[i]] = i
        arr = sorted([c for c in s], key=lambda x : idx[x] if x in idx else -1)
        return "".join(arr)