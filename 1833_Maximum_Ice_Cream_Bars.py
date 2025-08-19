class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        k = max(costs)
        cnts = [0] * (k+1)
        for val in costs:
            cnts[val] += 1
        for i in range(1,k+1):
            cnts[i] += cnts[i-1]
        arr = [0] * len(costs)
        for val in reversed(costs):
            arr[cnts[val] - 1] = val
            cnts[val] -= 1
        i = 0
        cost = arr[0]
        while i < len(arr) and cost <= coins:
            i += 1
            cost += arr[i] if i < len(arr) else 0
        return i