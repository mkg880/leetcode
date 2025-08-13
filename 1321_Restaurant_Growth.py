import pandas as pd
from datetime import timedelta

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values(by='visited_on')
    first_date = df.iloc[0]['visited_on']
    lim = first_date + timedelta(days=6)
    last_date = df.iloc[-1]['visited_on']
    if lim > last_date:
        return pd.DataFrame({})
    j = 0
    total = 0
    while j < len(df) and df.iloc[j]['visited_on'] <= lim:
        total += df.iloc[j]['amount']
        j += 1
    dates, amounts, averages = [lim], [total], [round(total / 7, 2)]
    i = 0
    lim += timedelta(days=1)
    while lim <= last_date:
        while j < len(df) and df.iloc[j]['visited_on'] <= lim:
            total += df.iloc[j]['amount']
            j += 1
        prev = lim + timedelta(days=-6)
        while df.iloc[i]['visited_on'] < prev:
            total -= df.iloc[i]['amount']
            i += 1
        dates.append(lim)
        amounts.append(total)
        averages.append(round(total / 7, 2))
        lim += timedelta(days=1)
    return pd.DataFrame({'visited_on': dates, 'amount': amounts, 'average_amount': averages})