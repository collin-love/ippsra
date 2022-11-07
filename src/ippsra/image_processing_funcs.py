"""Functions that will be used for determining the amount of bounding boxes
in an image thus allowing for the summation of how many found stones/boulders
/imperfections in the image.
"""
import cv2 as cv
import numpy as np
import bounding


class ImageAnalysis():

    @classmethod
    def __init__(self):
        """Sets the threshold values for the various rankings of the density
        of bounding boxes in an image.
        """
        # self.dangerous_threshold = 0.4
        self.risky_threshold = 0.25
        self.allowable_threshold = 0.1
        self.hazard_area_threshold = 15000  # pixels
        self.test_img = './data/images/render/render9327.png'
        self.thresh = 200

# NEED TO UPDATE TO TAKE IN IMG
    def num_hazards(self):
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
        delta_x, delta_y, hazard_count = bounding.thresh_callback(self.thresh)
        # IMG == DRAWING IN REINAS CODE
        # img = np.asarray(img)
        # rows = np.any(img, axis=1)
        # cols = np.any(img, axis=0)
        # rmin = np.argmax(rows)
        # rmax = img.shape[0] - 1 - np.argmax(np.flipud(rows))
        # cmin = np.argmax(cols)
        # cmax = img.shape[1] - 1 - np.argmax(np.flipud(cols))

        return delta_x, delta_y, hazard_count

# NEED TO UPDATE TO TAKE IN IMG
    def size_hazards(self):
        """Computes the absolute area that is covered by bounding boxes.

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: total area encompassed by the bounding boxes in an image.
        """
        delta_x, delta_y, hazard_count = self.num_hazards()
        # area = (rmax - rmin) * (cmax - cmin)
        # area = np.absolute(area)
        area = []
        for i in range(len(delta_x)):
            area_i = delta_x[i]*delta_y[i]
            area.append(area_i)
            if area[i] > self.hazard_area_threshold:
                area[i] = 0

        haz_area_tot = sum(area)
        return haz_area_tot
        # return area

# NEED TO UPDATE TO TAKE IN IMG
    def density_hazards(self):
        """Function to determine a ratio between the area covered by the
        hazards and the total area in the image.

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: Density ratio of area of bounding boxes to area of the image.
        """
        haz_area_tot = self.size_hazards()

        undoctored_img = cv.imread(self.test_img)
        # Extracting the height and width of an image
        h, w = undoctored_img.shape[:2]
        undoctored_area = np.absolute(h * w)
        density = np.absolute(haz_area_tot / undoctored_area)

        return density

# NEED TO UPDATE TO TAKE IN IMG
    def hazard_score(self):
        """The function for the ranking of images based on the detected hazards
        in the image. Currently, this is a ranking from the range of 1-3. This
        was chosen based on the simplicity of the ranking. By this it is
        simple to say that: the ranking 1 contains no obstructions in the image
        that is being processed, the ranking 2 contains less than 25% of
        coverage, and 3 is anything above 25%. (This is a generalization and
        is dependant on the size of the aircraft, but we have to assume a
        spacecraft size) We will work on exactly how this is determined

        Args:
            img (array): image containing the bounding boxes from 'bounding.py'

        Returns:
            int: The ranking of how the image ranks on the ranking scale (1-3)
        """
        density = self.density_hazards()
        if density <= self.allowable_threshold:
            score = 1  # Great score (1-3 scale ATM)
            return score
        elif density <= self.risky_threshold:
            score = 2  # Moderate score
            return score
        else:
            score = 3  # Bad score
            return score


print(ImageAnalysis().num_hazards())
print(ImageAnalysis().size_hazards())
print(ImageAnalysis().density_hazards())
print(ImageAnalysis().hazard_score())
