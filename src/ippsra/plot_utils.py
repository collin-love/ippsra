"""
    Visualization function to plot data created in plot_gtex.py. This file
    allows you to change the ylabel, xlabel, width, and height of the
    plot with the arguments at the top of the document
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import cv2 as cv
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
    
    Hazards = data['Number of Hazards']
    Density = data['Density of Hazards']
    Hazard_score = data['Hazard Score']

    fig1 = plt.figure(figsize=(6, 4), dpi=150)
    fig1, sns.violinplot(x=Hazard_score, y=Density)
    plt.show()

def show_img(img):
    img = cv.imread(img)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Original Gray', img_gray)
    cv.waitKey()


def show_obstruct(img):
    IA = ImageAnalysis()
    threshold = 200
    delta_x, delta_y, hazard_count, drawing = IA.bounding_box(img, threshold)
    img = cv.imread(img)
    # sidebyside = np.concatenate((img, drawing), axis=1)
    cv.imshow('Image with bounded Obstructions', drawing)
    cv.waitKey()
    return None

def concat_image(img):
    IA = ImageAnalysis()
    threshold = 200
    delta_x, delta_y, hazard_count, drawing = IA.bounding_box(img, threshold)
    img = cv.imread(img)
    sidebyside = np.concatenate((img, drawing), axis=1)
    cv.imshow('Original and Segmented', sidebyside)
    cv.waitKey()
    return None


if __name__ == '__main__':
    print("This doesn't work like that. Please use plot_utils.py as a module "
          + "in a script with the correct inputs.")