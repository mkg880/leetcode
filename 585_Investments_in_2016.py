import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    cities = {}
    for la, lo in zip(insurance['lat'], insurance['lon']):
        cities[(la, lo)] = cities.get((la, lo), 0) + 1
    m = {}
    res = 0
    for f, s, la, lo in zip(insurance['tiv_2015'], insurance['tiv_2016'], insurance['lat'], insurance['lon']):
        if f in m:
            if cities[(la, lo)] == 1:
                res += s
            res += m[f]
            m[f] = 0
        else:
            if cities[(la, lo)] == 1:
                m[f] = s
            else:
                m[f] = 0
    return pd.DataFrame({'tiv_2016': [round(res, 2)]})