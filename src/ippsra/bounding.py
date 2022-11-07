"""This script contains the first testing of finding different obstacles within
an image using OpenCV and python. Currently this script is only focusing on
one image now from a handpicked data set that contains clean, normal, and
obvious to the human eye images.
"""
import cv2 as cv
import numpy as np
import argparse
import random as rng
rng.seed(12345)


def thresh_callback(threshold):
    """Threshold function to process a contrasted image to create bounding
    boxes for the image. This will "find" the obstructions in an image.

    Args:
        threshold (int): The threshold value that will control where the
        bounding boxes will be placed on the image. This controls what is
        considered as an obstruction
    """

    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    contours, _ = cv.findContours(canny_output,
                                  cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3),
                       dtype=np.uint8)

    delta_x = []
    delta_y = []
    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])),
                     (int(boundRect[i][0]+boundRect[i][2]),
                      int(boundRect[i][1]+boundRect[i][3])), color, 2)
        delta_xi = int(boundRect[i][2])
        delta_x.append(delta_xi)
        delta_yi = int(boundRect[i][3])
        delta_y.append(delta_yi)
        # cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])),
        #           int(radius[i]), color, 2)

    hazard_count = len(contours)
    cv.imshow('Contours', drawing)
    # print(delta_x)
    return delta_x, delta_y, hazard_count


parser = argparse.ArgumentParser(description='Code for Creating Bounding '
                                 + 'boxes and circles for contours tutorial.')
parser.add_argument('--input', help='Path to input image.',
                    default='./data/images/render/render9327.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3, 3))
source_window = 'Source'
cv.namedWindow(source_window)
# cv.imshow(source_window, src)
max_thresh = 255
threshold = 200  # initial threshold

cv.createTrackbar('Canny thresh:', source_window, threshold, max_thresh,
                  thresh_callback)
thresh_callback(threshold)
# cv.waitKey()
