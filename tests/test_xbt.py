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
from pyxpr.xbt import XBT


class TestXBT(unittest.TestCase):
    """ Unit tests for the XBT class. """

    def setUp(self):
        self.xbt = XBT()

    def test_read(self):
        """ Check that the measured data is contextualised correctly. """
        path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                            "res", "XBT_00001.edf")
        self.xbt.read(path)

        assert((self.xbt.time ==
                numpy.array([0.0, 1.0, 1.5, 2.0, 2.5, 3.0])).all())
        assert((self.xbt.resistance ==
                numpy.array([500.0, 550.0, 487.5, 525.2, 662.1, 445.5])).all()
               )
        assert((self.xbt.depth ==
                numpy.array([0.0, 0.25, 0.56, 1.78, 2.64, 4.8])).all())
        assert((self.xbt.temperature ==
                numpy.array([28.5, 28.0, 27.35, 26.2, 23.4, 22])).all())
        assert((self.xbt.sound_velocity ==
                numpy.array([300.0, 300.0, 300.0, 300.0, 300.0, 300.0])).all()
               )

if(__name__ == "__main__"):
    unittest.main()
