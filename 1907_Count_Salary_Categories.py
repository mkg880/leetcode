import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    n = len(accounts)
    salaries = accounts['income']
    condition = salaries < 20000
    arr = [0] * 3
    arr[0] = condition.sum()
    condition = salaries > 50000
    arr[2] = condition.sum()
    arr[1] = n - arr[0] - arr[2]
    m = {"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": arr}
    return (pd.DataFrame(m))