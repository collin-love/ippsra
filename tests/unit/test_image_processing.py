"""Unittest for the image_processing module that contains most of the functions
used to rank the images once they are processed.
"""
import unittest
import random
import numpy as np
import sys
sys.path.append('./src/ippsra')
import image_processing_funcs  # nopep8
# import bounding  # nopep8


class TestAlgoDev(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hazard_count = 1
        cls.hazard_count_false = 3
        # cls.files = ['.png']  # WHAT IMAGE ?
        cls.img = bounding.thresh_callback(files)  # NEED TO RETURN DRAWING!!
        cls.hazard_size = 150  # NEED TO CHECK
        cls.hazard_size_false = 150  # NEED TO CHECK
        cls.hazard_density = 0.5  # NEED TO CHECK
        cls.hazard_density_false = 0.5  # NEED TO CHECK
        cls.hazard_score = 1  # NEED TO CHECK
        cls.hazard_score_false = 3  # NEED TO CHECK

    @classmethod
    def tearDownClass(cls):
        cls.hazard_count = None
        cls.hazard_count_false = None
        cls.files = None
        cls.img = None
        cls.hazard_size = None
        cls.hazard_size_false = None
        cls.hazard_density = None
        cls.hazard_density_false = None
        cls.hazard_score = None
        cls.hazard_score_false = None

    def test_num_hazards(self):
        self.assertTrue(
            image_processing_funcs.ImageAnalysis.num_hazards(self.img),
            self.hazard_count)

        self.assertFalse(
            image_processing_funcs.ImageAnalysis.num_hazards(self.img),
            self.hazard_count_false)

    def test_size_hazards(self):
        self.assertTrue(
            image_processing_funcs.ImageAnalysis.size_hazards(self.img),
            self.hazard_size)

        self.assertFalse(
            image_processing_funcs.ImageAnalysis.size_hazards(self.img),
            self.hazard_size_false)

    def test_density_hazards(self):
        self.assertTrue(
            image_processing_funcs.ImageAnalysis.density_hazards(self.img),
            self.hazard_density)

        self.assertFalse(
            image_processing_funcs.ImageAnalysis.density_hazards(self.img),
            self.hazard_density_false)

    def test_hazard_score(self):
        self.assertTrue(
            image_processing_funcs.ImageAnalysis.hazard_score(self.img),
            self.hazard_score)

        self.assertFalse(
            image_processing_funcs.ImageAnalysis.hazard_score(self.img),
            self.hazard_score_false)


if __name__ == '__main__':
    unittest.main()
