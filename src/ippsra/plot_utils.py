"""
    Visualization function to plot data created in plot_gtex.py. This file
    allows you to change the ylabel, xlabel, width, and height of the
    plot with the arguments at the top of the document
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import cv2 as cv
from imutils import build_montages
import sys
sys.path.append('./src/ippsra')
from image_processing_funcs import ImageAnalysis  # nopep8


# Width of figures
width = 6
height = 4

# X and Y label for the scatter plot
ylabel_scat = 'Density of Hazards'
xlabel_scat = 'Number of Hazards'

# Sets the style for seaborn more at
# https://www.python-graph-gallery.com/all-charts/
sns.set(style="darkgrid")


def scatter_plot(data):
    """A scatter plot to show the relationship between the number of hazards

    Args:
        data (csv): The data file created from the rank_images script
    """
    alpha = 0.3
    Hazards = data['Number of Hazards']
    Density = data['Density of Hazards']
    Hazard_score = data['Hazard Score']

    fig, ax = plt.subplots(dpi=150)
    scatter = ax.scatter(Hazards, Density, c=Hazard_score, cmap='cool',
                         alpha=0.3)
    fig, plt.ylabel(ylabel_scat)
    fig, plt.xlabel(xlabel_scat)
    # fig, plt.legend()
    legend1 = ax.legend(*scatter.legend_elements(), title="Ranking")

    ax.add_artist(legend1)
    plt.show()


def violinplot(data):
    """A violin plot to show the distribution of the hazard score

    Args:
        data (csv): The data file created from the rank_images script
    """
    Density = data['Density of Hazards']
    Hazard_score = data['Hazard Score']

    fig1 = plt.figure(dpi=150)
    fig1, sns.violinplot(x=Hazard_score, y=Density)
    plt.show()


def show_img(img):
    """This function shows an image in the window

    Args:
        img (file name): The image that you would like to show
    """
    img = cv.imread(img)
    cv.imshow('Original Image', img)
    cv.waitKey()


def show_obstruct(img):
    """A function to show the image with the bounding boxes of the obstructions

    Args:
        img (file name): The image that you would like to show with the
        bounding boxes drawn
    """
    IA = ImageAnalysis()
    threshold = 200
    delta_x, delta_y, hazard_count, drawing = IA.bounding_box(img, threshold)
    img = cv.imread(img)
    cv.imshow('Image with bounded obstructions', drawing)
    cv.waitKey()


def concat_image(img):
    """A function to concatenate an original image with an image that contains
    the bounding boxes of the obstructions

    Args:
        img (file name): The image that you would like to show with the
        original image and the image with the bounding boxes
    """
    IA = ImageAnalysis()
    threshold = 200
    delta_x, delta_y, hazard_count, drawing = IA.bounding_box(img, threshold)
    img = cv.imread(img)
    sidebyside = np.concatenate((img, drawing), axis=1)
    cv.imshow('Original | Bounding Boxes Drawn', sidebyside)
    cv.waitKey()


def compilation_rank(imageDir, one_hazard, two_hazard, three_hazard):
    """_summary_

    Args:
        imageDir (_type_): _description_
        one_hazard (_type_): _description_
        two_hazard (_type_): _description_
        three_hazard (_type_): _description_
    """
    # Defining used lists
    one_hazard_images = []
    two_hazard_images = []
    three_hazard_images = []
    scored_images = []

    # loop over the image paths and place them in one of the lists
    i = 0
    for _ in range(len(one_hazard)):
        one_hazard_path = os.path.join(imageDir,
                                       one_hazard['Image Name'][i])
        image = cv.imread(one_hazard_path)
        one_hazard_images.append(image)
        i = i + 1

    i = 0
    for _ in range(len(two_hazard)):
        two_hazard_path = os.path.join(imageDir,
                                       two_hazard['Image Name'][i])
        image = cv.imread(two_hazard_path)
        two_hazard_images.append(image)
        i = i + 1

    i = 0
    for _ in range(len(three_hazard)):
        three_hazard_path = os.path.join(imageDir,
                                         three_hazard['Image Name'][i])
        image = cv.imread(three_hazard_path)
        three_hazard_images.append(image)
        i = i + 1

    # create a montage using 200x200 "tiles" with 3 rows and 3 columns
    i = 0
    for img in range(len(one_hazard)):
        img = one_hazard_images[i]
        img = cv.resize(img, (400, 400))
        # writing the image with the hazard score -- using cv2.putText() and
        # some other formatting to make it look nice
        scored_images.append(
            cv.putText(img, "{:.2f}".format(one_hazard['Hazard Score'][i]),
                       (35, 35), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            )
        i = i + 1

    i = 0
    for img in range(len(two_hazard)):
        img = two_hazard_images[i]
        img = cv.resize(img, (400, 400))
        scored_images.append(
            cv.putText(img, "{:.2f}".format(two_hazard['Hazard Score'][i]),
                       (35, 35), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            )
        i = i + 1

    i = 0
    for img in range(len(three_hazard)):
        img = three_hazard_images[i]
        img = cv.resize(img, (400, 400))
        scored_images.append(
            cv.putText(img, "{:.2f}".format(three_hazard['Hazard Score'][i]),
                       (35, 35), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            )
        i = i + 1

    # convert scored_images to a numpy array of select images
    selected_images = [scored_images[1], scored_images[2], scored_images[3],
                       scored_images[(len(one_hazard) + 2)],
                       scored_images[(len(one_hazard) + 3)],
                       scored_images[(len(one_hazard) + 4)],
                       scored_images[(len(one_hazard) + len(two_hazard) + 2)],
                       scored_images[(len(one_hazard) + len(two_hazard) + 3)],
                       scored_images[(len(one_hazard) + len(two_hazard) + 4)]]
    cv.imshow("Ranked Compilation",
              build_montages(selected_images, (200, 200), (3, 3))[0])
    cv.waitKey(0)


if __name__ == '__main__':
    print("This doesn't work like that. Please use plot_utils.py as a module "
          + "in a script with the correct inputs.")
