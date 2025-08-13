class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # arr = [[True, True, True] for _ in range(n)]
        arr = {}
        for row, col in reservedSeats:
            if row not in arr:
                arr[row] = [True, True, True]
            if 2 <= col < 6:
                arr[row][0] = False
            if 4 <= col < 8:
                arr[row][1] = False
            if 6 <= col < 10:
                arr[row][2] = False
        res = 0
        for a, b, c in arr.values():
            if a and c:
                res += 2
            elif a or b or c:
                res += 1
        return res + 2 * (n - len(arr))
        