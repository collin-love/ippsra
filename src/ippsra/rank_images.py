"""Script to iterate through a directory of data and input the images into
a useable array
"""
import os
import sys
import cv2
import glob
import argparse
sys.path.append('./src/ippsra')
from image_processing_funcs import ImageAnalysis  # nopep8


def get_args():

    parser = argparse.ArgumentParser(description='Code for ranking a '
                                     + 'directory of images on a custom scale '
                                     + 'that is defined at this following '
                                     + 'link https://github.com/collin-love/'
                                     + 'ippsra/blob/main/README.md')
    parser.add_argument('--Directory', '-D', default='./data/test_data',
                        help='The PATH to the directory containing the images '
                        + 'that are going to be processed')
    parser.add_argument('--Extension', '-ext', default='png',
                        help='A list of the extensions for the image data '
                        + 'that is present in the directory for processing',
                        choices=['bmp', 'dib', 'jpeg', 'jpg', 'png', 'webp',
                                 'pbm', 'pgm', 'ppm', 'pxm', 'pnm', 'sr',
                                 'ras', 'tiff', 'tif', 'exr', 'hdr', 'pic'])

    return parser.parse_args()


def rank_images():
    """
    """
    args = get_args()

    imageDir = args.Directory
    ext = args.Extension

    # Check to see if the directory exists and if there are images in it
    if os.path.exists(imageDir) is False:
        raise OSError("This directory does not exist")
    # Checking if the dir is empty or not
    dir = os.listdir(imageDir)  # listing the contents
    if len(dir) == 0:
        raise OSError("This directory is empty")

    # iterate through the directory and rank the images

    for ext in os.listdir(imageDir):
        imagePath = os.path.join(imageDir, ext)

        ImageAnalysis().bounding_box(img=imagePath, threshold=200)
        print(ImageAnalysis().num_hazards(img=imagePath, threshold=200))
        print(ImageAnalysis().density_hazards(img=imagePath, threshold=200))
        print(ImageAnalysis().hazard_score(img=imagePath, threshold=200))

    # ImageAnalysis().show_img(img=imagePath)
    # ImageAnalysis().show_bbox(img=imagePath)


if __name__ == '__main__':
    rank_images()
