import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    s = queue.sort_values(by=['turn'])
    i = 0
    val = 0
    while i < len(s):
        val += s.iloc[i]['weight']
        if val > 1000:
            break
        i += 1
    return pd.DataFrame({'person_name': [s.iloc[i-1]['person_name']]})