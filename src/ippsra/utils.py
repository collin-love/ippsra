""" This script contains the utils for the processing of images with the help
of opencv and python packages
"""
import cv2


def test(A):
    x = print(A)
    return x


image_dir = r'./data/images/clean/clean0006.png'
real_images = cv2.imread(image_dir)
# Extracting the height and width of an image
h, w = real_images.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))
print('this Utils ran')
