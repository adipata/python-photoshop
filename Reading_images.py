from statistics import median

from matplotlib import image
from matplotlib import pyplot

import numpy as np

image = image.imread('img_small.jpg')
img = np.array(image)

'''
Exxercise 1
'''

print(image.shape)
print(image.dtype)

# Show image
pyplot.imshow(image)
pyplot.show()

'''
Exercise 2
'''

for y in range(0, image.shape[0] - 1):
    for x in range(0, image.shape[1] - 1):
        m = median(img[y][x])
        img[y][x][0] = m
        img[y][x][1] = m
        img[y][x][2] = m

pyplot.imshow(img)
pyplot.savefig('img_bw.png')
pyplot.show()


