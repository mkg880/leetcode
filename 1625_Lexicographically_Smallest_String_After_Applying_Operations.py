class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        stack = [s]
        visited = set()
        res = s
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            res = min(res, curr)
            one = ""
            for i in range(len(curr)):
                c = curr[i]
                if i % 2 == 1:
                    val = int(c)
                    val += a
                    one += str(val % 10)
                else:
                    one += c
            stack.append(one)
            two = curr[-b:] + curr[:-b]
            stack.append(two)
        return res