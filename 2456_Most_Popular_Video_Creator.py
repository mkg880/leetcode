class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m = {}
        for a, b, c in zip(creators, ids, views):
            if a not in m:
                m[a] = (-c, b, -c)
            else:
                x, y, z = m[a]
                if -c < z or (-c == z and b < y):
                    y = b
                    z = -c
                x -= c
                m[a] = (x, y, z)
        arr = sorted([(m[key], key) for key in m])
        val = arr[0][0][0]
        i = 1
        res = []
        while i < len(arr) and arr[i][0][0] == val:
            i += 1
        for a, b in arr[:i]:
            _, y, _ = a
            res.append([b, y])
        return res