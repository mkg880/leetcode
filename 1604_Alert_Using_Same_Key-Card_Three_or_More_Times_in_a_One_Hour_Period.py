class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def cmp(x):
            h, m = x.split(":")
            return int(h) * 60 + int(m)
        def timeDiff(a, b):
            h1, m1 = a.split(":")
            h2, m2 = b.split(":")
            return ((int(h2) - int(h1)) * 60 + (int(m2) - int(m1))) <= 60
        res = []
        m = {}
        for name, time in zip(keyName, keyTime):
            if name not in m:
                m[name] = []
            m[name].append(time)
        for key in m:
            arr = sorted(m[key], key=cmp)
            for i in range(2, len(arr)):
                if timeDiff(arr[i-2], arr[i]):
                    res.append(key)
                    break
        return sorted(res)