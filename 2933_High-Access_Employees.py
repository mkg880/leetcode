class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        arr = sorted([(int(time[:2]) * 60 + int(time[2:]), name) for name, time in access_times])
        m = {}
        res = set()
        for t, name in arr:
            if name not in m:
                m[name] = (None, t)
            else:
                if m[name][0] is not None and t - m[name][0] < 60:
                    res.add(name)
                m[name] = (m[name][1], t)
        return list(res)