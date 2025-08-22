class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = sorted([c - r for c, r in zip(capacity, rocks)])
        i = 0
        while i < len(arr) and additionalRocks >= 0:
            additionalRocks -= arr[i]
            i += 1
        return i-1 if additionalRocks < 0 else i