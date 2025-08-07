import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    prev = None
    cnt = 0
    res = []
    for num in logs['num']:
        if num in res:
            cnt = 0
            continue
        if prev is not None and num == prev:
            cnt += 1
            if cnt == 3:
                res.append(num)
        else:
            prev = num
            cnt = 1
    return pd.DataFrame({'ConsecutiveNums': res})