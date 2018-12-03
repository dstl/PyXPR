#!/usr/bin/env python

"""
(C) Crown Copyright 2018 Defence Science and Technology Laboratory UK

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading
data produced by expendable oceanographic profilers/probes and stored in
Lockheed Martin Sippican MK21 Export Data Format (EDF).

PyXPR is released under the MIT license. See the file LICENSE.md for more
information.
"""

from .probe import Probe


class XBT(Probe):
    """ Represents an eXpendable Bathymetric Thermograph (XBT) probe. """

    def read(self, path):
        """ Read and contextualise XBT data.
        :arg str path: The path to the probe's associated EDF file.
        """

        Probe.read(self, path)

        # Check that this data is indeed from an XBT.
        assert(self.type == "T-7" or self.type == "Fast Deep")

        # Get the columns of interest and contextualise them.
        self.time = self.data[:, 0].astype(float)
        self.resistance = self.data[:, 1].astype(float)
        self.depth = self.data[:, 2].astype(float)
        self.temperature = self.data[:, 3].astype(float)
        self.sound_velocity = self.data[:, 4].astype(float)

        return
