import numpy as np
import matplotlib.pyplot as plt
import argparse


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4, plot=False):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                       '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        self.c_len = len(self.colors)
        self.fig = plt.figure()
        self.fig.set_size_inches(10, 10)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.plot = plot

    def fit(self, X: np.ndarray):
        try:
            ids = np.random.choice(len(X), size=self.ncentroid, replace=False)
            self.centroids = np.array([X[i] for i in ids])

            for iter in range(self.max_iter):
                diffs = self.predict(X)
                for idx, centre in enumerate(self.centroids):
                    centre += np.average(X[diffs == idx] - centre, axis=0)
                    color = self.colors[idx % self.c_len]
                    self.__plot(X[diffs == idx], centre, color)
                if (self.plot):
                    plt.pause(0.1)
                if (iter < self.max_iter - 1):
                    self.ax.clear()
            if (self.plot):
                plt.show()
        except Exception:
            return

    def __plot(self, v, v2, color, is_cluster=0):
        self.ax.scatter(v[:, 0], v[:, 1], v[:, 2], c=color, marker=None)
        self.ax.scatter(v2[0], v2[1], v2[2], s=100, c=color, marker=(5, 1))

    def predict(self, X: np.ndarray):
        try:
            p = [np.argmin(np.abs(x - self.centroids).sum(axis=1)) for x in X]
            return np.array(p)
        except Exception:
            return

    def get_centroids(self):
        return self.centroids

    def get_centroids_average(self, X):
        d = self.predict(X)
        return [np.average(X[d == i], axis=0) for i in range(self.ncentroid)]


def get_regions(average):
    regions = []
    average = [[i, e] for i, e in enumerate(average)]
    average.sort(reverse=True, key=lambda x: x[1][0] - x[1][2])
    elm = average.pop(0)
    regions.insert(elm[0], 'Asteroids Belt colonies')
    average.sort(key=lambda x: x[1][1])
    if (average[1][1][0] <= average[2][1][0]):
        regions.insert(average[0][0], 'The flying cities of Venus')
        regions.insert(average[1][0], 'United Nations of Earth')
        regions.insert(average[2][0], 'Mars Republic')
    else:
        regions.insert(average[1][0], 'The flying cities of Venus')
        regions.insert(average[2][0], 'United Nations of Earth')
        regions.insert(average[0][0], 'Mars Republic')
    return regions


try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', type=str, required=True)
    parser.add_argument('-n', '--ncentroid', type=int, default=4)
    parser.add_argument('-m', '--max_iter', type=int, default=20)
    parser.add_argument('-p', '--plot', action='store_true', default=False)
    args = parser.parse_args()

    file = args.filepath
    cols = (1, 2, 3)
    my_data = np.genfromtxt(file, delimiter=',', skip_header=1, usecols=cols)
    kmc = KmeansClustering(args.max_iter, args.ncentroid,  args.plot)
    kmc.fit(my_data)

    regions = []
    if (args.ncentroid == 4):
        regions = get_regions(kmc.get_centroids_average(my_data))

    predicted_data = kmc.predict(my_data)
    for idx, centre in enumerate(kmc.get_centroids()):
        assoc_vec = my_data[predicted_data == idx]
        print('centroid', idx, ':', centre, '<-', assoc_vec.__len__())
        if (args.ncentroid == 4):
            print('region:', regions[idx])

except Exception:
    exit()
