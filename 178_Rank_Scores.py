import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    a = sorted(list(scores['score']), reverse=True)
    m = {}
    i = 1
    prev = None
    for score in a:
        if prev is not None and score == prev:
            continue
        m[score] = i
        i += 1
        prev = score
    s = []
    r = []
    for score in a:
        s.append(score)
        r.append(m[score])
    return pd.DataFrame({'score': s, 'rank': r})