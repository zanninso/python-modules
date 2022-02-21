import numpy as np


class ColorFilter:
    def invert(self, array: np.ndarray):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            for y, elm in enumerate(array):
                for x, elm in enumerate(array[y]):
                    array[y][x] = 1 - array[y][x]
                    array[y][x][3] = 1 - array[y][x][3]
            return array
        except Exception:
            return None

    def to_blue(self, array: np.ndarray):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            shape = (array.shape[0], array.shape[1], 2)
            return np.dstack((np.zeros(shape), array[::, ::, 2:]))
        except Exception:
            return None

    def to_green(self, array: np.ndarray):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            array = array.__deepcopy__(array)
            for y, elm in enumerate(array):
                for x, elm in enumerate(array[y]):
                    array[y][x][0], array[y][x][2] = 0, 0
            return array
        except Exception:
            return None

    def to_red(self, array: np.ndarray):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            new_array = self.to_green(array)
            for y, elm in enumerate(new_array):
                for x, elm in enumerate(new_array[y]):
                    new_array[y][x][0], new_array[y][x][1] = array[y][x][0], 0

            return new_array
        except Exception:
            return None

    def to_celluloid(self, array: np.ndarray):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            start = 0
            end = 1
            step = (end - start)/4
            c_range = np.arange(0.0, 1.001, step)
            for y, elm in enumerate(array):
                for x, elm in enumerate(array[y]):
                    array[y][x][0] = min(c_range, key=lambda x: abs(x-elm[0]))
                    array[y][x][1] = min(c_range, key=lambda x: abs(x-elm[1]))
                    array[y][x][2] = min(c_range, key=lambda x: abs(x-elm[2]))
            return array
        except Exception:
            return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        try:
            r, g, b = 1, 1, 1
            if (filter in ['w', 'weight']):
                r, g, b = kwargs['weights']
                print(kwargs['weights'])
            for y, elm in enumerate(array):
                for x, elm in enumerate(array[y]):
                    gry = sum([elm[0] * r, elm[1] * g, elm[2] * b]) / 3
                    array[y][x][0], array[y][x][1], array[y][x][2] = [gry] * 3
            return array
        except Exception:
            return None
