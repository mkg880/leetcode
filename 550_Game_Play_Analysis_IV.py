import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    dates = activity.groupby('player_id')['event_date']
    cnt = 0
    for d in dates:
        _, s = d
        a = np.array(s)
        if len(a) < 2:
            continue
        a.sort()
        temp = a[0] + pd.to_timedelta('1 day')
        if temp == a[1]:
            cnt += 1
    return pd.DataFrame({"fraction": [round(cnt / len(dates), 2)]})