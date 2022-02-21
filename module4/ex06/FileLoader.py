from build import re
import pandas as pd


class Fileloader:
    def __init__(self):
        pass

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print(df.shape)
            dim = re.sub("(\\(|\\))", '', str(df.shape)).replace(', ', ' x ')
            print('Loading dataset of dimensions {}'.format(dim))
            return df
        except Exception:
            None

    def display(self, df: pd.DataFrame, n: int):
        try:
            if isinstance(df, pd.DataFrame) is False:
                raise Exception()
            if isinstance(n, int) is False:
                raise Exception()
            print(df[:n: bool(n > 0) - bool(n < 0)])
        except Exception:
            return
