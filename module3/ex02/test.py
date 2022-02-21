import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0, 25).reshape(5, 5)
print('array:', arr1, '\n--------')
print('corped_array:', spb.crop(arr1, (3, 1), (1, 0)), '\n--------')
print()


arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print('array:', arr2, '\n--------')
print('thined_array:', spb.thin(arr2, 3, 0), '\n--------')


arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
arr2[2][3] = "P"
print('array:', arr2, '\n--------')
print('thined_array:', spb.thin(arr2, 3, 1), '\n--------')

arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print('array:', arr3, '\n--------')
print('thined_array:', spb.juxtapose(arr3, 3, 1), '\n--------')


arr4 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print('array:', arr4, '\n--------')
print('thined_array:', spb.mosaic(arr4, [3, 2]), '\n--------')
