class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        add = 2
        curr = 0
        res = []
        while curr + add <= finalSum:
            res.append(add)
            curr += add
            add += 2
        res[-1] += finalSum - curr
        return res