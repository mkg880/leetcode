class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0
        for log in logs:
            idx, func, time = log.split(':')
            idx = int(idx)
            time = int(time)
            if func == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(idx)
                prev = time
            else:
                old_idx = stack.pop()
                res[old_idx] += time - prev + 1
                prev = time + 1
        return res