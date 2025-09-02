class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        val = 2 * (2 * min(x, y) + z)
        return val + 2 if x != y else val