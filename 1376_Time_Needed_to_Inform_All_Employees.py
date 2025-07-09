class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = {}
        for i in range(len(manager)):
            if manager[i] not in children:
                children[manager[i]] = []
            children[manager[i]].append(i)
        res = 0
        def rec(node, curr):
            nonlocal res
            if node not in children:
                res = max(res, curr)
                return
            for child in children[node]:
                rec(child, curr + informTime[node])
        rec(headID, 0)
        return res