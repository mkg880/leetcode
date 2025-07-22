class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total = 0
        for seat, student in zip(seats, students):
            total += abs(seat - student)
        return total