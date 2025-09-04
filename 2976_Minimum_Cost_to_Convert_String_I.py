class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[float('inf')] * 26 for i in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for i in range(len(original)):
            a = ord(original[i]) - ord('a')
            b = ord(changed[i]) - ord('a')
            graph[a][b] = min(graph[a][b], cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        ans = 0
        for i in range(len(source)):
            val = graph[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
            if val == float('inf'):
                return -1
            ans += val
        return ans