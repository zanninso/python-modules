import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = None
        if (isinstance(df, pd.DataFrame)):
            self.df = df

    def when(self, location: str):
        try:
            if isinstance(location, str) is False:
                raise Exception()
            if (self.df is not None):
                df = self.df
                result = df.loc[df['City'] == location, 'Year']
                return result.drop_duplicates().tolist()
        except Exception as e:
            return

    def where(self, date: int):
        try:
            if isinstance(date, int) is False:
                raise Exception()
            if (self.df is not None):
                df = self.df
                result = df.loc[df['Year'] == date, 'City']
                return result.drop_duplicates().tolist()
        except Exception as e:
            return
