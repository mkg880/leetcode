import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['prev_day'] = weather['recordDate'] - np.timedelta64(1, 'D')
    return weather.merge(weather, how='inner', left_on='prev_day', right_on='recordDate').query('temperature_x > temperature_y')[['id_x']].rename(columns={'id_x': 'Id'})