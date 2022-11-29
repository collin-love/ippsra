"""Functions that will be used for determining the amount of bounding boxes
in an image thus allowing for the summation of how many found stones/boulders
/imperfections in the image.
"""
import cv2 as cv
import numpy as np
import random as rng

# defined thresh here to change values
thresh = 200


class ImageAnalysis():

    @classmethod
    def __init__(cls):
        """Sets the threshold values for the various rankings of the density
        of bounding boxes in an image.
        """
        cls.risky_threshold = 0.1
        cls.allowable_threshold = 0.05
        cls.hazard_area_threshold = 15000  # bboxes too large to be hazards
        cls.test_img = './data/images/render/render9327.png'
        cls.thresh = 200  # default threshold passed in

    def bounding_box(self, img, threshold=thresh):
        """Threshold function to process a contrasted image to create bounding
        boxes for the image. This will "find" the obstructions in an image.

        Args:
            threshold (int): This argument is optional and set to a default
            if no parameter is applied. The threshold value that will control
            where the bounding boxes will be placed on the image. This controls
            what is considered as an obstruction.

            img (png): image to be segmented with bounding boxes
        """
        img = cv.imread(cv.samples.findFile(img))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        image = cv.blur(img, (3, 3))
        canny_output = cv.Canny(image, threshold, threshold * 2)
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
            color = (rng.randint(0, 256),
                     rng.randint(0, 256),
                     rng.randint(0, 256))
            cv.drawContours(drawing, contours_poly, i, color)
            cv.rectangle(drawing,
                         (int(boundRect[i][0]),
                          int(boundRect[i][1])),
                         (int(boundRect[i][0]+boundRect[i][2]),
                          int(boundRect[i][1]+boundRect[i][3])),
                         color, 2)
            delta_xi = int(boundRect[i][2])
            delta_x.append(delta_xi)
            delta_yi = int(boundRect[i][3])
            delta_y.append(delta_yi)

        hazard_count = len(contours)
        # cv.imshow('Contours', drawing)
        return delta_x, delta_y, hazard_count, drawing

    def num_hazards(self, img, threshold=thresh):
        """This function takes in the .png image containing the bounding
        boxes from 'bounding.py'. It then iterates through a masked numpy
        array (array containing ones and zeros) to identify locations of
        bounding boxes. From here it will return coordinates of bounding
        boxes, of which we can analyze further to provide more intuition.

        Args:
            img (png): undoctored image we want segmented

            threshold (int): This argument is optional and set to a default
            if no parameter is applied. The threshold value that will control
            where the bounding boxes will be placed on the image. This controls
            what is considered as an obstruction.

        Returns:
            int: number of bounding boxes.
        """
        delta_x, delta_y, hazard_count, drawing = self.bounding_box(img,
                                                                    threshold)

        return hazard_count

    def density_hazards(self, img, threshold=thresh):
        """Function to determine a ratio between the area covered by the
        hazards and the total area in the image.

        Args:
            img (png): undoctored image we want segmented

            threshold (int): This argument is optional and set to a default
            if no parameter is applied. The threshold value that will control
            where the bounding boxes will be placed on the image. This controls
            what is considered as an obstruction.

        Returns:
            float: Density ratio of area of bounding boxes to area of image.
        """
        delta_x, delta_y, hazard_count, drawing = self.bounding_box(img,
                                                                    threshold)
        undoctored_img = cv.imread(img)

        # Extracting the height and width of an image
        h, w = undoctored_img.shape[:2]
        undoctored_area = np.absolute(h * w)

        area = []
        for i in range(len(delta_x)):
            area_i = delta_x[i]*delta_y[i]
            area.append(area_i)
            if area[i] > self.hazard_area_threshold:
                area[i] = 0

        haz_area_tot = sum(area)
        density = round(np.absolute(haz_area_tot / undoctored_area), 2)

        return density

    def hazard_score(self, img, threshold=thresh):
        """The function for the ranking of images based on the detected hazards
        in the image. Currently, this is a ranking from the range of 1-3. This
        was chosen based on the simplicity of the ranking. By this it is
        simple to say that: the ranking 1 contains no obstructions in the image
        that is being processed, the ranking 2 contains less than 25% of
        coverage, and 3 is anything above 25%. (This is a generalization and
        is dependant on the size of the aircraft, but we have to assume a
        spacecraft size) We will work on exactly how this is determined

        Args:
            img (png): undoctored image we want segmented

            threshold (int): This argument is optional and set to a default
            if no parameter is applied. The threshold value that will control
            where the bounding boxes will be placed on the image. This controls
            what is considered as an obstruction.

        Returns:
            int: The ranking of how the image ranks on the ranking scale (1-3)
        """
        density = self.density_hazards(img, threshold)
        if density <= self.allowable_threshold:
            score = 1  # Great score (1-3 scale ATM)
            return score
        elif density <= self.risky_threshold:
            score = 2  # Moderate score
            return score
        else:
            score = 3  # Bad score
            return score
