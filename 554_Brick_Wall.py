class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = {}
        maxVal = 0
        for row in wall:
            loc = 0
            for i in range(len(row) - 1):
                val = row[i]
                loc += val
                cnt[loc] = cnt.get(loc, 0) + 1
                maxVal = max(cnt[loc], maxVal)
        return len(wall) - maxVal