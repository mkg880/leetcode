import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales['rank'] = sales.groupby('product_id').year.rank(method='dense')
    return sales.loc[sales['rank'] == 1][['product_id', 'year', 'quantity', 'price']].rename(columns={'year': 'first_year'})