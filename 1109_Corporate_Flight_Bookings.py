class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n+1)
        for first, last, seats in bookings:
            arr[first - 1] += seats
            arr[last] -= seats
        res = [0] * n
        curr = 0
        for i in range(n):
            curr += arr[i]
            res[i] = curr
        return res