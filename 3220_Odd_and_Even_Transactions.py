import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    res = {'transaction_date': [], 'odd_sum': [], 'even_sum': []}
    for name, group in transactions.groupby('transaction_date'):
        res['transaction_date'].append(name)
        odd, even = 0, 0
        for val in group['amount']:
            if val % 2 == 0:
                even += val
            else:
                odd += val
        res['even_sum'].append(even)
        res['odd_sum'].append(odd)
    return pd.DataFrame(res)