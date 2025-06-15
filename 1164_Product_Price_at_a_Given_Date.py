import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    before = products.query('change_date <= \'2019-08-16\'')
    last = before.loc[before.groupby('product_id').change_date.idxmax()].rename(columns={'new_price': 'price'})[['product_id', 'price']]
    excluded = products[~products.product_id.isin(last.product_id)][['product_id']].drop_duplicates()
    excluded['price'] = 10
    print(excluded)
    return pd.concat([last, excluded], axis=0)