from sys import stderr
from time import sleep
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    def load(self, path: str) -> numpy.ndarray:
        try:
            array = numpy.array(plt.imread(path))
            print("Loading image of dimensions {} x {}".format(*array.shape))
            return array
        except Exception as e:
            print(e, file=stderr)
            return None

    def display(self, array: numpy.ndarray):
        try:
            plt.axis('off')
            plt.imshow(array)
            plt.show()
        except Exception as e:
            print(e, file=stderr)
            return None
