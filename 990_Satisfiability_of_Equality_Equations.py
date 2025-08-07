class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        id = {}
        def find(x):
            id[x] = id.get(x, x)
            while x != id[x]:
                x = id[x]
            return x
        def merge(x, y):
            id[x] = id.get(x, x)
            id[y] = id.get(y, y)
            id[find(x)] = find(y)
        eq = [(eq[0], eq[3]) for eq in equations if eq[1] == '=']
        neq = [(eq[0], eq[3]) for eq in equations if eq[1] == '!']
        for a, b in eq:
            merge(a, b)
        for a, b in neq:
            if find(a) == find(b):
                return False
        return True
