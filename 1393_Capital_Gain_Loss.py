import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.loc[stocks['operation'] == 'Buy', ['price']] = -stocks.loc[stocks['operation'] == 'Buy', ['price']]
    return stocks.groupby('stock_name').price.sum().reset_index().rename(columns={'price': 'capital_gain_loss'})