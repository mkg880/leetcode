class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        stack = [k]
        sus = set()
        while stack:
            x = stack.pop()
            if x in sus:
                continue
            sus.add(x)
            stack.extend(graph[x])
        for i in range(n):
            if i not in sus and any(x in sus for x in graph[i]):
                return list(range(n))
        return list(set(range(n)) - sus)