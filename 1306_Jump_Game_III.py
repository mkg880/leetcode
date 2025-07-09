class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = set()
        while stack:
            loc = stack.pop()
            if loc in visited or loc < 0 or loc >= len(arr):
                continue
            visited.add(loc)
            if arr[loc] == 0:
                return True
            stack.append(loc + arr[loc])
            stack.append(loc - arr[loc])
        return False