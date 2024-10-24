class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 1
        amt = 0
        min_val = amt
        min_idx = 0
        while i < len(gas):
            amt = amt - cost[i-1] + gas[i-1]
            if amt < min_val:
                min_val = amt
                min_idx = i
            i = i + 1
        i = (min_idx + 1) % len(gas)
        amt = 0
        counter = 0
        while counter < len(gas):
            amt = amt - cost[(i-1) % len(gas)] + gas[(i-1) % len(gas)]
            print(amt)
            if amt < 0:
                return -1
            i = (i+1) % len(gas)
            counter += 1
        return min_idx