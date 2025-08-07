class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def inc(x):
            if x == '9':
                return '0'
            return str(int(x) + 1)
        def dec(x):
            if x == '0':
                return '9'
            return str(int(x) - 1)
        
        vis = set(deadends)
        q = deque([('0000', 0)])
        while q:
            arr, dist = q.popleft()
            if arr in vis:
                continue
            vis.add(arr)
            if arr == target:
                return dist
            for i in range(4):
                q.append((arr[:i] + inc(arr[i]) + arr[i+1:], dist + 1))
                q.append((arr[:i] + dec(arr[i]) + arr[i+1:], dist + 1))
        return -1