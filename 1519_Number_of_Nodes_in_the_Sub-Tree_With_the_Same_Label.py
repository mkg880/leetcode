class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        desc = {}
        for a, b in edges:
            if a not in desc:
                desc[a] = []
            if b not in desc:
                desc[b] = []
            desc[a].append(b)
            desc[b].append(a)
        res = [0] * n
        visited = set()
        def rec(node):
            m = {}
            if node is None or node in visited:
                return m
            visited.add(node)
            m[labels[node]] = 1
            for child in desc.get(node, []):
                child_map = rec(child)
                for key in child_map:
                    m[key] = m.get(key, 0) + child_map[key]
            res[node] = m[labels[node]]
            return m
        rec(0)
        return res