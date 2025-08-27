class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        m = {-1: float('inf')}
        curr = node1
        cnt = 0
        while curr not in m:
            m[curr] = cnt
            cnt += 1
            curr = edges[curr]
        m2 = {-1: float('inf')}
        curr = node2
        cnt = 0
        while curr not in m2:
            m2[curr] = cnt
            cnt += 1
            curr = edges[curr]
        res = -1
        minVal = float('inf')
        for key in m:
            if key in m2:
                val = max(m[key], m2[key])
                if val < minVal or (val == minVal and key < res):
                    res = key
                    minVal = val
        return res