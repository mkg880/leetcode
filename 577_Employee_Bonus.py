import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(bonus, how='left', left_on='empId', right_on='empId').query('bonus < 1000 | bonus.isnull()')[['name', 'bonus']]