import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.set_index('personId').join(address.set_index('personId')).drop('addressId', axis=1)