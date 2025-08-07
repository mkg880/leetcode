class MapSum:

    def __init__(self):
        self.m = {}
        self.vals = {}

    def insert(self, key: str, val: int) -> None:
        m = self.m
        for c in key + '/':
            if c in m:
                m = m[c]
            else:
                m[c] = {}
                m = m[c]
        self.vals[key] = val
    def sum(self, prefix: str) -> int:
        m = self.m
        for c in prefix:
            if c not in m:
                return 0
            m = m[c]
        res = 0
        stack = [(m, prefix)]
        while stack:
            m, s = stack.pop()
            if '/' in m:
                res += self.vals[s]
            for key in m:
                if key == '/':
                    continue
                stack.append((m[key], s + key))
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)