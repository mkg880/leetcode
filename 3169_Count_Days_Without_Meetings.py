class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        new_meetings = []
        start, end = meetings[0]
        for i in range(1, len(meetings)):
            if meetings[i][0] <= end:
                end = max(end, meetings[i][1])
            else:
                new_meetings.append([start, end])
                start, end = meetings[i]
        new_meetings.append([start, end])
        res = new_meetings[0][0] - 1
        for i in range(1, len(new_meetings)):
            if new_meetings[i][0] > new_meetings[i-1][1]:
                res += new_meetings[i][0] - new_meetings[i-1][1] - 1
        if days > new_meetings[-1][1]:
            res += days - new_meetings[-1][1]
        return res