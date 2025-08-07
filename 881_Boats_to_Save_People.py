class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        res = 0
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
            res += 1
            j -= 1
        if i == j:
            res += 1
        return res