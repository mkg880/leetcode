import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree['test'] = tree['id'].isin(tree['p_id'])
    tree['type'] = tree['test'].apply(lambda x: 'Inner' if x else 'Leaf')
    tree.loc[tree['p_id'].isnull(), 'type'] = 'Root'
    return tree[['id', 'type']]
    