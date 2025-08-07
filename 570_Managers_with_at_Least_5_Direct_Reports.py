import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    m = {}
    for manager in employee['managerId']:
        m[manager] = m.get(manager, 0) + 1
    res = []
    for key, val in m.items():
        if val >= 5:
            names = employee[employee['id'] == key]['name']
            if not names.empty:
                print(names)
                res.append(names.iloc[0])
    return pd.DataFrame({'name': res})