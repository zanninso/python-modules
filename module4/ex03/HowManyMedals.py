from cmath import nan
import pandas as pd


def _sort(x):
    return(sorted(x, key=lambda x: ['S', 'B', 'G'].index(x)))


def howManyMedals(df: pd.DataFrame, name: str):
    try:
        if isinstance(df, pd.DataFrame) is False:
            raise Exception()
        if isinstance(name, str) is False:
            raise Exception()
        df = df.loc[df['Name'] == name, ['Year', 'Medal']]
        group = df.groupby(['Year', 'Medal'], dropna=False)
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
