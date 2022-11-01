"""Functions that will be used for determining the amount of bounding boxes
in an image thus allowing for the summation of how many found stones/boulders
/imperfections in the image.
"""
import cv2 as cv
import numpy as np


class ImageAnalysis():
    @classmethod
    def __init__(self):
        """Sets the threshold values for the various rankings of the density
        of bounding boxes in an image.
        """
        # self.dangerous_threshold = 0.4
        self.risky_threshold = 0.25
        self.allowable_threshold = 0.1

    def num_hazards(self, img):
        """This function takes in the .png image containing the bounding
        boxes from 'bounding.py'. It then iterates through a masked numpy
        array (array containing ones and zeros) to identify locations of
        bounding boxes. From here it will return coordinates of bounding
        boxes, of which we can analyze further to provide more intuition.

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            array: coordinates of bounding boxes.
        """
        # IMG == DRAWING IN REINAS CODE
        img = np.asarray(img)

        rows = np.any(img, axis=1)
        cols = np.any(img, axis=0)
        rmin = np.argmax(rows)
        rmax = img.shape[0] - 1 - np.argmax(np.flipud(rows))
        cmin = np.argmax(cols)
        cmax = img.shape[1] - 1 - np.argmax(np.flipud(cols))

        return rmin, rmax, cmin, cmax

    def size_hazards(self, img):
        """Computes the absolute area that is covered by bounding boxes.

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: total area encompassed by the bounding boxes in an image.
        """
        rmin, rmax, cmin, cmax = self.num_hazards(img)
        area = (rmax - rmin) * (cmax - cmin)
        area = np.absolute(area)
        return area

    def density_hazards(self, img):
        """Function to determine a ratio between the area covered by the
        hazards and the total area in the image.

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: Density ratio of area of bounding boxes to area of the image.
        """
        area = self.size_hazards(img)

        undoctored_img = cv.imread(img)
        # Extracting the height and width of an image
        h, w = undoctored_img.shape[:2]
        undoctored_area = np.absolute(h * w)
        density = np.absolute(area / undoctored_area)

        return density

    def hazard_score(self, img):
        """The function for the ranking of images based on the detected hazards
        in the image. Currently, this is a ranking from the range of 1-3. This
        was chosen based on the simplicity of the ranking. The 

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: The ranking of how the image ranks on the ranking scale (1-3)
        """
        density = self.density_hazards(img)
        if density <= self.allowable_threshold:
            score = 1  # Great score (1-3 scale ATM)
            return score
        elif density <= self.risky_threshold:
            score = 2  # Moderate score
            return score
        else:
            score = 3  # Bad score
            return score
