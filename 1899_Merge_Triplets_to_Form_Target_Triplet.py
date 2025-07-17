class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one, two, three = False, False, False
        x, y, z = target
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            if a == x:
                one = True
            if b == y:
                two = True
            if c == z:
                three = True
            if one and two and three:
                return True
        return False