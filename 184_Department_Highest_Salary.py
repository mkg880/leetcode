import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    dep = {}
    for _, row in department.iterrows():
        dep[row['id']] = row['name']
    m = {}
    for _, row in employee.iterrows():
        curr, _ = m.get(row['departmentId'], [float('-inf'), []])
        if curr < row['salary']:
            m[row['departmentId']] = [row['salary'], [row['name']]]
        elif curr == row['salary']:
            m[row['departmentId']][1].append(row['name'])
    d, e, s = [], [], []
    for key in m:
        salary, names = m[key]
        for name in names:
            d.append(dep[key])
            e.append(name)
            s.append(salary)
    return pd.DataFrame({'Department': d, 'Employee': e, 'Salary': s})