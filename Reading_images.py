from statistics import median

from matplotlib import image
from matplotlib import pyplot

import numpy as np

image = image.imread('img_small.jpg')

'''
Exxercise 1: Reading images
'''
img = np.array(image)

print(image.shape)
print(image.dtype)

# Show image
pyplot.imshow(image)
pyplot.show()

'''
Exercise 2: conversion to grayscale
'''
img = np.array(image)

for y in range(0, image.shape[0] - 1):
    for x in range(0, image.shape[1] - 1):
        m = median(img[y][x])
        img[y][x][0] = m
        img[y][x][1] = m
        img[y][x][2] = m

pyplot.imshow(img)
pyplot.savefig('img_bw.png')
pyplot.show()

'''
Exercide 2: Thresholds
'''
img = np.array(image)

for y in range(0, image.shape[0] - 1):
    for x in range(0, image.shape[1] - 1):
        m = median(img[y][x])
        if m > 128:
            m = 255
        else:
            m = 0
        img[y][x][0] = m
        img[y][x][1] = m
        img[y][x][2] = m

pyplot.imshow(img)
pyplot.savefig('img_silhouette.png')
pyplot.show()

'''
Exercise 3: Finding edges
'''
img = np.array(image)
img2 = np.array(image)

for y in range(1, image.shape[0] - 2):
    for x in range(1, image.shape[1] - 2):
        mr = median([img[y - 1][x - 1][0], img[y - 1][x][0], img[y - 1][x + 1][0], img[y][x - 1][0], img[y][x][0],
                     img[y][x + 1][0], img[y + 1][x - 1][0], img[y + 1][x][0], img[y + 1][x + 1][0]])
        mg = median([img[y - 1][x - 1][1], img[y - 1][x][1], img[y - 1][x + 1][1], img[y][x - 1][1], img[y][x][1],
                     img[y][x + 1][1], img[y + 1][x - 1][1], img[y + 1][x][1], img[y + 1][x + 1][1]])
        mb = median([img[y - 1][x - 1][2], img[y - 1][x][2], img[y - 1][x + 1][2], img[y][x - 1][2], img[y][x][2],
                     img[y][x + 1][2], img[y + 1][x - 1][2], img[y + 1][x][2], img[y + 1][x + 1][2]])
        if abs(int(median([mr, mg, mb])) - int(median([img[y][x][0], img[y][x][1], img[y][x][2]]))) > 10:
            img2[y][x][0] = 255
            img2[y][x][1] = 0
            img2[y][x][2] = 0

pyplot.imshow(img2)
pyplot.savefig('img_edge.png')
pyplot.show()

'''
Exercise 4: Be creative
'''
img = np.array(image)
img2 = np.array(image)

for y in range(7, image.shape[0] - 7):
    for x in range(7, image.shape[1] - 7):
        mra = []
        mga = []
        mba = []
        for i in range(y - 6, y + 6):
            for j in range(x - 6, x + 6):
                mra.append(int(img[i][j][0]))
                mga.append(int(img[i][j][1]))
                mba.append(int(img[i][j][2]))
        mr = median(mra)
        mg = median(mga)
        mb = median(mba)

        img2[y][x][0] = mr
        img2[y][x][1] = mg
        img2[y][x][2] = mb

pyplot.imshow(img2)
pyplot.savefig('img_blur.png')
pyplot.show()

img = np.array(image)

for y in range(0, image.shape[0] - 1):
    for x in range(0, image.shape[1] - 1):
        m = median(img[y][x])
        img[y][x][0] = 0
        img[y][x][1] = m
        img[y][x][2] = round(m/4)

pyplot.imshow(img)
pyplot.savefig('img_matrix.png')
pyplot.show()
