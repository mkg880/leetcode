class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        m = {}
        parent = {}
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1:
                m[i] = [l]
                if l in parent:
                    return False
                parent[l] = i
            if r != -1:
                m[i] = m.get(i, []) + [r]
                if r in parent or l == r:
                    return False
                parent[r] = i
        if n - len(parent) != 1:
            return False
        for i in range(n):
            if i not in parent:
                root = i
                break
        stack = [root]
        vis = set()
        while stack:
            node = stack.pop()
            if node in vis:
                return False
            vis.add(node)
            stack += m.get(node, [])
        return len(vis) == n