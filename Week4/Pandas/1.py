import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    group = actor_director.groupby(['actor_id', 'director_id'])
    counts = group.size()
    filtered = counts[counts >= 3]
    res = filtered.reset_index()[['actor_id', 'director_id']]
    return res
