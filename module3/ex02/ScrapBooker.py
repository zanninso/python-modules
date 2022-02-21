import numpy as np
from numpy import ndarray


class ScrapBooker:

    def crop(self, array: ndarray, dim: tuple, position: tuple = (0, 0)):
        try:
            if isinstance(array, np.ndarray) is False:
                raise Exception()
            if (len(dim) != 2):
                raise Exception()
            if (len(position) != 2):
                raise Exception()
            height, width = dim
            y, x = position
            return(array[y:y + height, x:x + width])
        except Exception:
            return

    def thin(self, array: np.ndarray, n: int, axis: int):
        try:
            if isinstance(array, np.ndarray) is False:
                raise Exception()
            row, col = array.shape
            if (axis not in [0, 1]):
                raise Exception()
            if n <= 0 or (axis == 0 and n >= row) or (axis == 1 and n >= col):
                raise Exception()
            if axis == 0:
                a1, a2 = array[::, :n-1], array[::, n:]
                return np.array([np.append(lh, rh) for lh, rh in zip(a1, a2)])
            if (axis == 1):
                return np.vstack((array[:n-1, ::], array[n:, ::]))
        except Exception:
            return

    def juxtapose(self, array: np.ndarray, n: int, axis: int):
        try:
            if isinstance(array, np.ndarray) is False:
                raise Exception()
            if (axis not in [0, 1]):
                raise Exception()
            if n <= 0:
                raise Exception()
            if axis == 0:
                return np.tile(array, [n, 1])
            else:
                return np.tile(array, n)
        except Exception:
            return

    def mosaic(self, array: np.array, dim: tuple):
        try:
            if isinstance(array, np.ndarray) is False:
                raise Exception()
            if len(dim) != 2:
                raise Exception()
            return np.tile(array, list(dim))
        except Exception:
            return
