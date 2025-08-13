class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items = sorted(list(set([x[2] for x in orders])))
        m = {}
        for _, table, item in orders:
            table = int(table)
            if table not in m:
                m[table] = {}
            m[table][item] = m[table].get(item, 0) + 1
        res = [["Table"] + items]
        for key in sorted(m.keys()):
            arr = [str(key)]
            for item in items:
                arr.append(str(m[key].get(item, 0)))
            res.append(arr)
        return res