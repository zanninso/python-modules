from cmath import nan
import pandas as pd
import pdb


def _sort(x):
    return(sorted(x, key=lambda x: ['S', 'B', 'G'].index(x)))


def howManyMedalsByCountry(df: pd.DataFrame, country: str):
    try:
        if isinstance(df, pd.DataFrame) is False:
            raise Exception()
        if isinstance(country, str) is False:
            raise Exception()
        fields = ['Year', 'Team', 'Medal', 'Games', 'Sport', 'Event']
        df = df.loc[df['Team'] == country, fields].drop_duplicates()
        group = df[['Year', 'Medal']].groupby(['Year', 'Medal'], dropna=False)
        result = group.size()
        result = result.rename({'Bronze': 'B', 'Gold': 'G', 'Silver': 'S'})
        result = result.unstack(level='Year')
        for key in ['S', 'B', 'G']:
            if key not in result.index.array:
                result.loc[key] = 0
        result.drop(labels=[nan], errors='ignore', inplace=True)
        result.fillna(0, inplace=True)
        result.sort_index(key=_sort, inplace=True)
        return result.astype('int64').to_dict()
    except Exception as e:
        return
