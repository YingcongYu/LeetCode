# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.


import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'id':sorted(views[views['author_id'] == views['viewer_id']]['author_id'].unique())})
