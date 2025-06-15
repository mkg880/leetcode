import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first = delivery.loc[delivery.groupby('customer_id').order_date.idxmin()]
    res = round(len(first.loc[first.customer_pref_delivery_date == first.order_date]) / len(first) * 100, 2)
    return pd.DataFrame({"immediate_percentage": [res]})