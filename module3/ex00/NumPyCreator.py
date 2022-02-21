from random import randint
import numpy as np
import warnings
warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)


class NumPyCreator:

    def from_list(self, lst):
        '''takes list or nested list, returns its corresponding Numpy array,'''
        if (isinstance(lst, list)):
            try:
                return np.array(lst)
            except Exception:
                return None
        return None

    def from_tuple(self, tpl):
        '''takes tuple or nested one, returns its corresponding Numpy array'''
        if (isinstance(tpl, tuple)):
            try:
                return np.array(tpl)
            except Exception:
                return None
        return None

    def from_iterable(self, itr):
        '''takes iterable, returns array which contains all of its elements'''
        try:
            return np.array(itr)
        except Exception:
            return None

    def from_shape(self, shape, value=0):
        '''returns an array filled with the same value,
        The first argument is a tuple which specifies the shape of the array,
        and the second argument
        specifies the value of all the elements.
        This value must be 0 by default,'''
        try:
            return np.full(shape, value)
        except Exception:
            return None

    def random(self, shape):
        '''returns an array filled with random values,
        It takes as an argument tuple which specifies the shape of the array'''
        try:
            return np.random.rand(*shape)
        except Exception:
            return None

    def identity(self, n):
        '''returns an array representing the identity matrix of size n.'''
        try:
            return np.identity(n)
        except Exception:
            return None
