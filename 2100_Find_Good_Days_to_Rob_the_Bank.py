class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        non_inc = [1]
        curr = 1
        for i in range(1, n):
            if security[i] <= security[i-1]:
                curr += 1
            else:
                curr = 1
            non_inc.append(curr)
        non_dec = [1] * n
        curr = 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                curr += 1
            else:
                curr = 1
            non_dec[i] = curr
        return [i for i in range(n) if non_inc[i] > time and non_dec[i] > time]