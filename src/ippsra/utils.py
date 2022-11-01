""" This script contains the utils for the processing of images with the help
of opencv and python packages
"""
import cv2 as cv
import numpy as np
import random as rng
rng.seed(12345)

# Here for testing purposes only
def test(A):
    x = print(A)
    return x
image_dir = r'./data/images/clean/clean0006.png'
real_images = cv.imread(image_dir)
# Extracting the height and width of an image
h, w = real_images.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))
print('this Utils ran')
# End of testing block (can delete once new test are set)

