import pdb
from matplotlib import pyplot as plt
from numpy import NaN
import pandas as pd
from MyPlotLib import MyPlotLib
import pdb


class Komparator:
    def __init__(self, df) -> None:
        self.df = None
        if isinstance(df, pd.DataFrame):
            self.df = df

    def compare_histograms(self, cat_var, num_var):
        '''plots one histogram for each numerical feature in the list'''
        df = self.df
        try:
            if df is None:
                raise Exception('invalid dataframe')
            c = df.columns
            t = df.dtypes
            if (type(cat_var) == str and type(num_var) == str) is False:
                raise Exception('params type invalid')
            if (cat_var in c and num_var in c) is False:
                raise Exception('field name incorrect')
            if t[num_var] in [int, float] is False:
                raise Exception('fields types invalid')
            groups = df[[cat_var, num_var]].groupby([cat_var]).groups
            length = 0
            for group in groups:
                length = max(length, len(groups[group]))
            for group in groups:
                diff_len = length - len(groups[group])
                groups[group] = groups[group].to_list() + ([NaN] * diff_len)
            df = pd.DataFrame.from_dict(groups)
            MyPlotLib().histogram(df, df.columns.tolist())
        except Exception as e:
            return

    def density(self, cat_var, num_var):
        '''plots the density curve of each numerical feature in the list,'''
        df = self.df
        try:
            if df is None:
                raise Exception('invalid dataframe')
            c = df.columns
            t = df.dtypes
            if (type(cat_var) == str and type(num_var) == str) is False:
                raise Exception('params type invalid')
            if (cat_var in c and num_var in c) is False:
                raise Exception('field name incorrect')
            if t[num_var] in [int, float] is False:
                raise Exception('fields types invalid')
            groups = df[[cat_var, num_var]].groupby([cat_var]).groups
            length = 0
            for group in groups:
                length = max(length, len(groups[group]))
            for group in groups:
                cu_len = len(groups[group])
                diff_len = length - len(groups[group])
                groups[group] = groups[group].to_list() + ([NaN] * diff_len)
            df = pd.DataFrame.from_dict(groups)
            MyPlotLib().density(df, df.columns.tolist())
        except Exception as e:
            return

    def compare_box_plots(self, cat_var, num_var):
        '''displays a box plot for each numerical variable in the dataset.'''
        df = self.df
        try:
            if df is None:
                raise Exception('invalid dataframe')
            c = df.columns
            t = df.dtypes
            if (type(cat_var) == str and type(num_var) == str) is False:
                raise Exception('params type invalid')
            if (cat_var in c and num_var in c) is False:
                raise Exception('field name incorrect')
            if t[num_var] in [int, float] is False:
                raise Exception('fields types invalid')
            groups = df[[cat_var, num_var]].groupby([cat_var]).groups
            length = 0
            for group in groups:
                length = max(length, len(groups[group]))
            for group in groups:
                cu_len = len(groups[group])
                diff_len = length - len(groups[group])
                groups[group] = groups[group].to_list() + ([NaN] * diff_len)
            df = pd.DataFrame.from_dict(groups)
            MyPlotLib().box_plot(df, df.columns.tolist())
        except Exception as e:
            return
