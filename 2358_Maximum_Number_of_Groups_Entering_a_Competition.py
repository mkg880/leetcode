from math import floor
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return floor(((8 * len(grades) + 1) ** 0.5 - 1) / 2)