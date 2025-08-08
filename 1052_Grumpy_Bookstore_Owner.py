class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        curr = 0
        for i in range(minutes):
            curr += customers[i]
        for i in range(minutes, n):
            if not grumpy[i]:
                curr += customers[i]
        res = curr
        for start in range(1, n - minutes + 1):
            if grumpy[start-1]:
                curr -= customers[start-1]
            if grumpy[start+minutes-1]:
                curr += customers[start+minutes-1]
            res = max(res, curr)
        return res
