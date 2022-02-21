from ImageProcessor import ImageProcessor
import numpy as np
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")
cf = ColorFilter()
imp.display(arr)
imp.display(cf.invert(np.array(arr)))
imp.display(cf.to_green(np.array(arr)))
imp.display(cf.to_red(np.array(arr)))
imp.display(cf.to_blue(np.array(arr)))
imp.display(cf.to_celluloid(np.array(arr)))
imp.display(cf.to_grayscale(np.array(arr), 'm'))
imp.display(cf.to_grayscale(np.array(arr), 'w', weights=[0.2, 0.3, 0.5]))
