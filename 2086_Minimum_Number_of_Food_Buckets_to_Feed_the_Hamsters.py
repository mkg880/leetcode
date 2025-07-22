class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        res = 0
        last_bucket = None
        for i in range(n):
            if hamsters[i] == 'H':
                if i > 0 and last_bucket == i-1:
                    continue
                l, r = (i > 0 and hamsters[i-1] == '.'), (i < n-1 and hamsters[i+1] == '.')
                if r:
                    last_bucket = i+1
                    res += 1
                elif l:
                    res += 1
                else:
                    return -1
        return res