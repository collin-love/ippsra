"""Script to iterate through a directory of data and input the images into
a useable array
"""
import os
import sys
import cv2
import glob
import argparse
sys.path.append('./src/ippsra')
import image_processing_funcs as ipf  # nopep8


def get_args():

    parser = argparse.ArgumentParser(description='Code for ranking a '
                                     + 'directory of images on a custom scale '
                                     + 'that is defined at this following '
                                     + 'link https://github.com/collin-love/'
                                     + 'ippsra/blob/main/README.md')
    parser.add_argument('--Directory', '-D', default='./data/test_data',
                        help='The PATH to the directory containing the images '
                        + 'that are going to be processed')
    parser.add_argument('--Extension', '-ext', default=['png', 'jpg'],
                        help='A list of the extensions for the image data '
                        + 'that is present in the directory for processing',
                        choices=['bmp', 'dib', 'jpeg', 'jpg', 'png', 'webp', 
                                 'pbm', 'pgm', 'ppm', 'pxm', 'pnm', 'sr', 
                                 'ras', 'tiff', 'tif', 'exr', 'hdr', 'pic'])

    return parser.parse_args()

def rank_images():
    
    args = get_args()

    imageDir = args.Directory
    ext = args.Extension

    if os.path.exists(imageDir) is False:
        raise OSError("This directory is empty")
    # Checking if the dir is empty or not
    dir = os.listdir(imageDir)  # listing the contents
    if len(dir) == 0:
        raise OSError("This directory is empty")

    Ims = []  # Setting up a list to add image data to
    [Ims.extend(glob.glob(imageDir + '*.' + e)) for e in ext]

    images = [cv2.imread(file) for file in Ims]

    print(images)
    print(imageDir, ext)

# imageDir = './data/test_data/'  # Dir for the test dataset
# ext = ['png', 'jpg']  # Different image formats
'''
def argparser(imageDir, ext=['png', 'jpg']):
    """Function to iterate through a directory of image data

    Args:
        imageDir (str): Directory for the dataset.
        ext (list, optional): Different image formats to check for. Defaults
        to ['png', 'jpg'].
    """
    # Checking if the directory exists
    if os.path.exists(imageDir) is False:
        raise OSError("This directory is empty")
    # Checking if the dir is empty or not
    dir = os.listdir(imageDir)  # listing the contents
    if len(dir) == 0:
        raise OSError("This directory is empty")

    Is = []  # Setting up a list to add image data to
    [Is.extend(glob.glob(imageDir + '*.' + e)) for e in ext]

    images = [cv2.imread(file) for file in Is]

    return images
'''


if __name__ == '__main__':
    rank_images()
