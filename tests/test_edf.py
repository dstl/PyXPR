#!/usr/bin/env python

"""
(C) Crown Copyright 2018 Defence Science and Technology Laboratory UK

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading
data produced by expendable oceanographic profilers/probes and stored in
Lockheed Martin Sippican MK21 Export Data Format (EDF).

PyXPR is released under the MIT license. See the file LICENSE.md for more
information.
"""

import unittest
import os
import numpy
from pyxpr.edf import EDF


class TestEDF(unittest.TestCase):
    """ Unit tests for the EDF class. """

    def setUp(self):
        self.edf = EDF()

    def test_read(self):
        """ Check that the header and data of an EDF file can be correctly
        read in and parsed. """
        path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                            "res", "XBT_00001.edf")
        self.edf.read(path)

        assert(len(self.edf.header) == 15)

        # Check that the header field names exist in the header dictionary.
        for field_name in ["Probe Type", "Test 1", "Test 2", "Test 3",
                           "12345", "Field 1", "Field 2", "Field 3",
                           "Field 4", "Field 5"]:
            assert(field_name in self.edf.header.keys())

        # Check that the data has been correctly read in.
        assert(self.edf.data.shape == (6, 5))
        expected_data = numpy.array([[0.0, 500.0, 0.0, 28.5, 300.0],
                                     [1.0, 550.0, 0.25, 28.0, 300.0],
                                     [1.5, 487.5, 0.56, 27.35, 300.0],
                                     [2.0, 525.2, 1.78, 26.2, 300.0],
                                     [2.5, 662.1, 2.64, 23.4, 300.0],
                                     [3.0, 445.5, 4.8, 22.0, 300.0]])
        # All values are read in as strings at this stage, and type casted
        # later.
        expected_data = expected_data.astype(str)
        assert((self.edf.data == expected_data).all())

if(__name__ == "__main__"):
    unittest.main()
