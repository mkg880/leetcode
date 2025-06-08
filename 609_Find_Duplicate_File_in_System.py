class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = {}
        res = []
        for s in paths:
            arr = s.split()
            for i in range(1, len(arr)):
                f = arr[i]
                o = f.find('(')
                c = f.find(')')
                path = f[:o]
                content = f[o+1:c]
                new_path = arr[0] + '/' + path
                if content in m:
                    m[content].append(new_path)
                else:
                    m[content] = [new_path]
        for key in m:
            if len(m[key]) > 1:
                res.append(m[key])
        return res