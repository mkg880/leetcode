class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        totals = [0] * 6
        top = [0] * 6
        bottom = [0] * 6
        max_cnt = 0
        max_val = 0
        for a, b in zip(tops, bottoms):
            a -= 1
            b -= 1
            top[a] += 1
            bottom[b] += 1
            totals[a] += 1
            if totals[a] > max_cnt:
                max_cnt = totals[a]
                max_val = a
            if a != b:
                totals[b] += 1
                if totals[b] > max_cnt:
                    max_cnt = totals[b]
                    max_val = b
        if max_cnt != n:
            return -1
        return min(n - top[max_val], n - bottom[max_val])
            