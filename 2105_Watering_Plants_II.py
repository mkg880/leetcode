class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        i = 0
        j = n - 1
        res = 0
        a = capacityA
        b = capacityB
        while i < j:
            if a < plants[i]:
                res += 1
                a = capacityA
            a -= plants[i]
            if b < plants[j]:
                res += 1
                b = capacityB
            b -= plants[j]
            i += 1
            j -= 1
        if i == j and max(a, b) < plants[i]:
            res += 1
        return res