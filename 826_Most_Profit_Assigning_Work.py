class Solution:
    def binary(self, arr, target):
        low = 0
        high = len(arr) - 1
        closest = None

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return arr[mid]

            if arr[mid] < target:
                closest = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return closest


    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = sorted([(i, j) for (i, j) in zip(difficulty, profit)])
        d = {}
        m = float('-inf')
        for (i, j) in arr:
            m = max(m, j)
            d[i] = m
        difficulty.sort()
        total = 0
        for i in worker:
            val = self.binary(difficulty, i)
            if val:
                total += d[val]
        return total

