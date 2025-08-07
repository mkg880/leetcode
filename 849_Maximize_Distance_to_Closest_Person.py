class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = -1
        next = -1
        res = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                last = i
            else:
                l = float('inf') if last == -1 else i - last
                r = float('inf')
                if next < len(seats):
                    if i > next:
                        next = i+1
                        while next < len(seats):
                            if seats[next] == 1:
                                r = next - i
                                break
                            next += 1
                    else:
                        r = next - i
                res = max(res, min(l, r))
        return res