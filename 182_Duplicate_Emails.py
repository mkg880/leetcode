import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.merge(person, how='left', left_on='email', right_on='email').query('id_x < id_y')[['email']].drop_duplicates(subset='email')