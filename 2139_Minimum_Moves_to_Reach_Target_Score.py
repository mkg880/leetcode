class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and maxDoubles:
            if target % 2 == 1:
                target -= 1
                res += 1
            target = target // 2
            res += 1
            maxDoubles -= 1
        return res + target - 1