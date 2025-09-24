class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        stack = []
        res = 0
        for i in range(len(maximumHeight)):
            prev = 1 if i == 0 else maximumHeight[i-1] + 1
            if maximumHeight[i] - 1 >= prev:
                stack.append((prev, maximumHeight[i] - 1))
            if i > 0 and maximumHeight[i] == maximumHeight[i-1]:
                if not stack:
                    return -1
                l, r = stack.pop()
                val = r
                r -= 1
                if r >= l:
                    stack.append((l, r))
            else:
                val = maximumHeight[i]
            res += val
        return res