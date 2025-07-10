class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        h = position[-1] - position[0]
        l = 1
        ans = -1
        while l <= h:
            mid = (h+l) // 2
            pos = position[0]
            cnt = 1
            for p in position:
                if p - pos >= mid:
                    pos = p
                    cnt += 1
            if cnt >= m:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans