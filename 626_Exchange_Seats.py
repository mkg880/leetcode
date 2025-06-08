import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    i = 0
    while i + 1 < len(seat):
        temp = seat['student'][i]
        seat['student'][i] = seat['student'][i+1]
        seat['student'][i+1] = temp
        i += 2
    return seat