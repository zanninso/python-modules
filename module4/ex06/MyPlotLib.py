import pdb
from matplotlib import pyplot as plt
import pandas as pd


class MyPlotLib:
    def __init__(self) -> None:
        pass

    def histogram(self, data, features):
        '''plots one histogram for each numerical feature in the list'''
        try:
            if isinstance(data, pd.DataFrame) is False:
                raise Exception()
            if isinstance(features, list) is False:
                raise Exception()
            if all([isinstance(f, str) for f in features]) is False:
                raise Exception()
            c = data.columns
            t = data.dtypes
            features = [f for f in features if f in c and t[f] in [int, float]]
            fig, axs = plt.subplots(1, len(features), tight_layout=True)
            if len(features) == 1:
                axs = [axs]
            for idx, f in enumerate(features):
                axs[idx].title.set_text(f)
                axs[idx].hist(data[f])
                axs[idx].grid()
            plt.show()
        except Exception as e:
            return

    def density(self, data, features):
        '''plots the density curve of each numerical feature in the list,'''
        try:
            if isinstance(data, pd.DataFrame) is False:
                raise Exception()
            if isinstance(features, list) is False:
                raise Exception()
            if all([isinstance(f, str) for f in features]) is False:
                raise Exception()
            c = data.columns
            t = data.dtypes
            features = [f for f in features if f in c and t[f] in [int, float]]
            for f in features:
                data[f].plot.density(label=f)
            plt.legend(prop={'size': 10})
            plt.show()
        except Exception as e:
            return

    def pair_plot(self, data, features):
        '''plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable against
        another one.
        The main diagonal of this matrix shows simple histograms.'''
        try:
            if isinstance(data, pd.DataFrame) is False:
                raise Exception()
            if isinstance(features, list) is False:
                raise Exception()
            if all([isinstance(f, str) for f in features]) is False:
                raise Exception()
            c = data.columns
            t = data.dtypes
            features = [f for f in features if f in c and t[f] in [int, float]]
            pd.plotting.scatter_matrix(data[features])
            plt.show()
        except Exception as e:
            return

    def box_plot(self, data, features):
        '''displays a box plot for each numerical variable in the dataset.'''
        try:
            if isinstance(data, pd.DataFrame) is False:
                raise Exception()
            if isinstance(features, list) is False:
                raise Exception()
            if all([isinstance(f, str) for f in features]) is False:
                raise Exception()
            c = data.columns
            t = data.dtypes
            features = [f for f in features if f in c and t[f] in [int, float]]
            data.boxplot(features)
            plt.show()
        except Exception as e:
            return
