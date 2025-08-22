class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        stack = [(0, [0] * 12, 11, numArrows)]
        max_score, res = 0, []
        while stack:
            score, arr, i, remaining = stack.pop()
            if i == -1:
                if score > max_score:
                    max_score = score
                    arr[0] += remaining
                    res = arr
                continue
            if aliceArrows[i] + 1 <= remaining:
                stack.append((score+i, arr[:i] + [aliceArrows[i] + 1] + arr[i+1:], i-1, remaining - aliceArrows[i] - 1))
            stack.append((score, arr, i-1, remaining))
        return res