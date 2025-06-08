import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.query('referee_id != 2 | referee_id.isnull()')[['name']]