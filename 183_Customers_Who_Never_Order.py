import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    return df[df.isnull().any(axis=1)][['name']].rename(columns={'name': 'Customers'})