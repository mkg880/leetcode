class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        m = {}
        res = []
        for name in names:
            if name not in m:
                m[name] = 0
                res.append(name)
            else:
                m[name] += 1
                while f"{name}({m[name]})" in m:
                    m[name] += 1
                res.append(f"{name}({m[name]})")
                m[f"{name}({m[name]})"] = 0
        return res