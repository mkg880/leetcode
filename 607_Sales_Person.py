import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    reds = orders.merge(company, how='inner', left_on='com_id', right_on='com_id').query('name == \'RED\'')['sales_id']
    return sales_person[~sales_person.sales_id.isin(reds)][['name']]