class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        cnt = 1
        end = ranges[0][1]
        for l, r in ranges[1:]:
            if l > end:
                cnt += 1
            end = max(end, r)
        return pow(2, cnt, 10 ** 9 + 7)