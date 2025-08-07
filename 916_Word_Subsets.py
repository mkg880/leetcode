class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = {}
        for word in words2:
            cnt = Counter(word)
            for key in cnt:
                m[key] = max(cnt[key], m.get(key, 0))
        res = []
        for word in words1:
            c = Counter(word)
            valid = True
            for key in m:
                if key not in c or c[key] < m[key]:
                    valid = False
                    break
            if valid:
                res.append(word)
        return res