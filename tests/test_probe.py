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
from pyxpr.probe import Probe


class TestProbe(unittest.TestCase):
    """ Unit tests for the Probe class. """

    def setUp(self):
        self.probe = Probe()
        self.header = {"Probe Type": "T-7", "Sequence Number": "00001",
                       "Latitude": "25 32.5N", "Longitude": "55 15.99W",
                       "Date of Launch": "10/01/2018",
                       "Time of Launch": "12:15:39"}

    def test_parse_metadata(self):
        """ Check that the header information is parsed correctly. """

        self.probe.parse_metadata(self.header)

        # Check the correctness of the parsed fields.
        assert(self.probe.type == self.header["Probe Type"])
        assert(self.probe.sequence_number == int(
                                             self.header["Sequence Number"]))

    def test_parse_latitude_longitude(self):
        """ Check that a probe's latitude and longitude can be converted from
        degrees decimal minutes to decimal degrees. """
        parsed = self.probe.parse_latitude_longitude(self.header["Latitude"])
        assert(parsed == 25.541666666666666666666666666667)
        parsed = self.probe.parse_latitude_longitude(self.header["Longitude"])
        assert(parsed == -55.2665)

if(__name__ == "__main__"):
    unittest.main()
