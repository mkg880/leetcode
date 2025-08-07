import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    a = sorted(list(set(employee['salary'])), reverse = True)
    val = a[N-1] if 0 <= N-1 < len(a) else None
    return pd.DataFrame({f"getNthHighestSalary({N})": [val]})
