class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adjList = {}
        for i in range(n):
            adjList[i] = [j for j in range(n) if isConnected[i][j] and i != j]
        res = 0
        for i in range(n):
            if i not in adjList:
                continue
            stack = [i]
            while stack:
                curr = stack.pop()
                if curr not in adjList:
                    continue
                for neighbor in adjList[curr]:
                    stack.append(neighbor)
                del adjList[curr]
            res += 1
        return res