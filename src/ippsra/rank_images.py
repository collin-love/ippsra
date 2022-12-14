"""Script to iterate through a directory of data and input the images into
a useable DataFrame
"""
import os
import sys
import pandas as pd
import cv2
import argparse
sys.path.append('./src/ippsra')
from image_processing_funcs import ImageAnalysis  # nopep8
import plot_utils as pu  # nopep8


def get_args():
    """A function that parses all the inputs from the user to be used in this
    script

    Returns:
        Argument Parser: The function to get the arguments from the user input
    """

    parser = argparse.ArgumentParser(description='Code for ranking a '
                                     + 'directory of images on a custom scale '
                                     + 'that is defined at this following '
                                     + 'link https://github.com/collin-love/'
                                     + 'ippsra/blob/main/README.md',
                                     formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)
    parser.add_argument('--Directory', '-D', default='./data/test_data',
                        help='The PATH to the directory containing the images '
                        + 'that are going to be processed')
    parser.add_argument('--Extension', '-ext', default='png',
                        help='A list of the extensions for the image data '
                        + 'that is present in the directory for processing',
                        choices=['bmp', 'dib', 'jpeg', 'jpg', 'png', 'webp',
                                 'pbm', 'pgm', 'ppm', 'pxm', 'pnm', 'sr',
                                 'ras', 'tiff', 'tif', 'exr', 'hdr', 'pic'])
    parser.add_argument('--csvPath', default='./data/processed_data',
                        help='The PATH to the directory where the CSV file '
                        + 'will be saved')
    parser.add_argument('--csvName', default='sorted_test.csv',
                        help='Then name of the CSV file that will be created')
    parser.add_argument('--fileName', default='./data/processed_data/Test_',
                        help='The test name for the file. ex: if '
                        + '--fileName test1_  then this would result in '
                        + 'test1_1_scatter.png')
    parser.add_argument('--save', default='False',
                        help='Boolean for if you want to save the files',
                        choices=['True', 'False'])
    parser.add_argument('--imgIdx', default='0',
                        help='The index of the image that you want to show at '
                        + 'the end of the script from a sorted list of images '
                        + 'from best to worst. The default is 0 (the best '
                        + 'ranked image)')
    parser.add_argument('--showImages', default='True',
                        help='Boolean for if you want to show images',
                        choices=['True', 'False'])
    parser.add_argument('--showPlots', default='True',
                        help='Boolean for if you want to plot the data',
                        choices=['True', 'False'])

    return parser.parse_args()


def rank_images():
    """The main script in this repository that will iterate through a directory
    and output ranked data to a CSV file in the name of the user's choice and
    location. As well as other plots with the use of the plot_utils.py script

    Raises:
        OSError: The specified directory does not exist
        OSError: The specified directory does not contain any images
        OSError: The specified directory has data created with the same
        specified name
        OSError: The directory that the CSV file is to be saved to does not
        exist
    """
    args = get_args()

    # Renaming the class function for ease of use
    IA = ImageAnalysis()
    # Adding all the arguments to variables for use in the script
    ext = args.Extension
    imageDir = args.Directory
    csvPath = args.csvPath
    csvName = args.csvName
    save = args.save
    showPlots = args.showPlots
    showImages = args.showImages
    fileName = args.fileName
    imgIdx = int(args.imgIdx)
    file_exists = os.path.exists(csvPath + '/' + csvName)

    # Check to see if a file already exists. Added here to fail fast
    if save == 'True' and file_exists is True:
        raise OSError(f'(OSError): The file {csvName} already exists in '
                      + f'the directory {csvPath}. Please move or delete '
                      + 'the file and try again')

    try:
        # Check to see if the data directory exists and is populated
        if os.path.exists(imageDir) is False:
            raise OSError(f'(OSError): The directory {imageDir} does not '
                          + 'exist')
        # Checking if the data dir is empty or not by listing the contents
        if len(os.listdir(imageDir)) == 0:
            raise OSError(f'(OSError): The directory {imageDir} is empty')
        # Check if the csv directory exists
        if os.path.exists(csvPath) is False:
            raise OSError(f'(OSError): The directory {csvPath} does not '
                          + 'exist')
    finally:
        # Creating an empty list to store the data
        Is = [[] for _ in range(len(os.listdir(imageDir)))]
        # Iterate through the directory and rank the images
        i = 0
        with os.scandir(imageDir) as image_dir:
            print(f'There are {len(os.listdir(imageDir))} images in this dir')
            for entry in image_dir:
                if entry.name.endswith(ext) and entry.is_file():
                    # Create the full OS path to the image
                    imagePath = os.path.join(imageDir, entry.name)
                    # Extend function to add the data to the empty list
                    Is[i].append(entry.name)
                    Is[i].append(IA.num_hazards(img=imagePath,
                                                threshold=200))
                    Is[i].append(IA.density_hazards(img=imagePath,
                                                    threshold=200))
                    Is[i].append(IA.hazard_score(img=imagePath,
                                                 threshold=200))
                if i % 20 == 0:
                    print(f'{i} images have been ranked')
                i = i + 1

        # Creating a header for the output file
        header = ['Image Name', 'Number of Hazards',
                  'Density of Hazards', 'Hazard Score']

        # Create a data frame from the nested lists
        image_info = pd.DataFrame(Is, columns=header, index=None)
        # Sort the data by the density of hazards
        sorted_image_info = image_info.sort_values(
            by='Density of Hazards', ascending=True)

        # Pull out all images that have a hazard score of 1
        filt_hazard_score = 1
        one_hazard = IA.single_hazards_list(filt_hazard_score,
                                            sorted_image_info)
        print(f'There are {len(one_hazard)} images with a hazard score of 1')
        # Pull out all images that have a hazard score of 2
        filt_hazard_score = 2
        two_hazard = IA.single_hazards_list(filt_hazard_score,
                                            sorted_image_info)
        print(f'There are {len(two_hazard)} images with a hazard score of 2')
        # Pull out all images that have a hazard score of 3
        filt_hazard_score = 3
        three_hazard = IA.single_hazards_list(filt_hazard_score,
                                              sorted_image_info)
        print(f'There are {len(three_hazard)} images with a hazard score of 3')

        # Setup all filenames for saving
        fileNameBest = os.path.join(fileName + 'best.png')
        fileNameWorst = os.path.join(fileName + 'worst.png')
        fileNameUser = os.path.join(fileName + 'user.png')
        fileNameComp = os.path.join(fileName + 'compilation.png')
        fileNameScat = os.path.join(fileName + 'scatter_plot.png')
        fileNameViol = os.path.join(fileName + 'violin_plot.png')
        fileNameSctVil = os.path.join(fileName + 'scat_viol.png')

        # Plot and show all the images if requested
        if showPlots == 'True':
            pu.scatter_plot(sorted_image_info, save, showPlots, fileNameScat)
            pu.violinplot(sorted_image_info, save, showPlots, fileNameViol)
            pu.scat_violin(sorted_image_info, save, showPlots, fileNameSctVil)

        # Show all images if requested
        if showImages == 'True':
            # Full path to the image that will be displayed
            best_img = os.path.join(imageDir,
                                    sorted_image_info['Image Name'].iloc[1])
            worst_img = os.path.join(imageDir,
                                     sorted_image_info['Image Name'].iloc[
                                         (len(one_hazard)
                                          + len(two_hazard) + 3)])

            # Show the best and worst images with bounding boxes
            pu.concat_image(best_img, save, showImages, fileNameBest)
            pu.concat_image(worst_img, save, showImages, fileNameWorst)

            # Display the user's choice of image
            usr_image = os.path.join(imageDir,
                                     sorted_image_info['Image Name'][imgIdx])
            pu.show_img(usr_image, save, showImages, fileNameUser)

            # Create a compilation of the ranked images
            pu.compilation_rank(imageDir, one_hazard, two_hazard,
                                three_hazard, save, showImages, fileNameComp)

        # Save the data frame to a csv file if the user specifies
        if save == 'True':
            # Save the raw data to a CSV file
            # Comment out if you don't want to save the raw data
            image_info.to_csv(os.path.join(csvPath, 'raw_data.csv'),
                              index=False)

            # Save a sorted version of the data to a CSV file with
            # the user's name
            sorted_image_info.to_csv(os.path.join(csvPath, csvName),
                                     index=False)

            # Full path to the image that will be displayed
            best_img = os.path.join(imageDir,
                                    sorted_image_info['Image Name'][0])
            worst_img = os.path.join(imageDir,
                                     sorted_image_info['Image Name'].iloc[-1])

            # Display the user's choice of image
            usr_image = os.path.join(imageDir,
                                     sorted_image_info['Image Name'][imgIdx])
            pu.show_img(usr_image, save, showImages, fileNameUser)

            # Show the best and worst images with bounding boxes
            pu.concat_image(best_img, save, showImages, fileNameBest)
            pu.concat_image(worst_img, save, showImages, fileNameWorst)

            # Create a compilation of the ranked images
            pu.compilation_rank(imageDir, one_hazard, two_hazard,
                                three_hazard, save, showImages, fileNameComp)
            # Plotting the data
            fileNameScat = os.path.join(fileName + 'scatter_plot.png')
            fileNameViol = os.path.join(fileName + 'violin_plot.png')
            pu.scatter_plot(sorted_image_info, save, showImages, fileNameScat)
            pu.violinplot(sorted_image_info, save, showImages, fileNameViol)
            pu.scat_violin(sorted_image_info, save, showPlots, fileNameSctVil)


if __name__ == '__main__':
    rank_images()
