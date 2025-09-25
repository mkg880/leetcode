from typing import List
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        arr = [bin(num)[2:] for num in nums]
        return max(int(arr[a] + arr[b] + arr[c], base=2) for a, b, c in [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])