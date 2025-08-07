import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    m = {}
    cnt = 0
    res = -1
    for x in pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']]):
        print(x)
        m[x] = m.get(x, 0) + 1
        if m[x] > cnt:
            cnt = m[x]
            res = x
    return pd.DataFrame({'id': [res], 'num': [cnt]})