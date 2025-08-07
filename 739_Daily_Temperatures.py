class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack:
                j, prev = stack[-1]
                if prev >= t:
                    break
                stack.pop()
                res[j] = i - j
            stack.append((i, t))
        return res