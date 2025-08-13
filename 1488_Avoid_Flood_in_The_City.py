class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_rain = {}
        dries = []
        choices = {}
        for i, x in enumerate(rains):
            if x == 0:
                dries.append(i)
            else:
                if x in last_rain:
                    idx = 0
                    while idx < len(dries) and dries[idx] < last_rain[x]:
                        idx += 1
                    if idx == len(dries):
                        return []
                    choices[dries[idx]] = x
                    dries.pop(idx)
                last_rain[x] = i
        res = []
        for i, x in enumerate(rains):
            if x != 0:
                res.append(-1)
            else:
                res.append(choices.get(i, 1))
        return res