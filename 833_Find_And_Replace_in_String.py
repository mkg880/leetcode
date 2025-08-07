class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = ''
        arr = sorted([(idx, src, tgt) for idx, src, tgt in zip(indices, sources, targets)])
        prev = 0
        for idx, src, tgt in arr:
            res += s[prev:idx]
            if s[idx:idx+len(src)] == src:
                res += tgt
                prev = idx+len(src)
            else:
                prev = max(prev, idx)
        res += s[prev:]
        return res