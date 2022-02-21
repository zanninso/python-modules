import pandas as pd


def youngestfellah(df: pd.DataFrame, year: int):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    try:
        if isinstance(df, pd.DataFrame) is False:
            raise Exception()
        if isinstance(year, int) is False:
            raise Exception()
        f = df.loc[(df['Sex'] == 'F') & (df['Year'] == year), 'Age'].min()
        m = df.loc[(df['Sex'] == 'M') & (df['Year'] == year), 'Age'].min()
        return {'f': f, 'm': m}
    except Exception as e:
        return
