import cv2 as cv
import numpy as np


class ImageAnalysis():
    @classmethod
    def __init__(self):
        # self.dangerous_threshold = 0.4
        self.risky_threshold = 0.25
        self.allowable_threshold = 0.1

    def num_hazards(self, img):
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
        rmin, rmax, cmin, cmax = self.num_hazards(img)
        area = (rmax - rmin) * (cmax - cmin)
        area = np.absolute(area)
        return area

    def density_hazards(self, img):
        area = self.size_hazards(img)

        undoctored_img = cv.imread(img)
        # Extracting the height and width of an image
        h, w = undoctored_img.shape[:2]
        undoctored_area = np.absolute(h * w)
        density = np.absolute(area / undoctored_area)

        return density

    def hazard_score(self, img):
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
