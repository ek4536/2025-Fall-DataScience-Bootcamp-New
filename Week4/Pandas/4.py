import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    if len(salaries) < 2:
        second_salary = None
    else:
        second_salary = salaries.iloc[1]

    return pd.DataFrame({'SecondHighestSalary':[second_salary]})
