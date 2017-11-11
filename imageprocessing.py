#%matplotlib inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# Generate c.jpg
imga = mpimg.imread('a.jpg')
imgb = mpimg.imread('b.jpg')

print imga.shape
print [imga.min(), imga.max()]
print imga.dtype

imgc_1 = imga[0:250, 0:600]
imgc_2 = imga[250:650, 0:100]
imgc_3 = imgb
imgc_4 = imga[250:650, 500:600]
imgc_5 = imga[650:900, 0:600]
imgc_234 = np.hstack((imgc_2, imgc_3, imgc_4))
imgc = np.vstack((imgc_1, imgc_234, imgc_5))

mpimg.imsave('c.jpg', imgc)
