import pandas as pd


def proportionBySport(df: pd.DataFrame, year: int, sport: str, gender: str):
    try:
        if isinstance(df, pd.DataFrame) is False:
            raise Exception()
        if isinstance(year, int) is False:
            raise Exception()
        if isinstance(sport, str) is False:
            raise Exception()
        if isinstance(gender, str) is False:
            raise Exception()
        fields = ['ID', 'Sport']
        f = df.loc[(df['Sex'] == gender) & (df['Year'] == year), fields]
        return f.loc[f['Sport'] == sport, 'ID'].nunique() / f['ID'].nunique()
    except Exception as e:
        print(e)
        return
