#!/usr/bin/env python

"""
(C) Crown Copyright 2017, 2018 Defence Science and Technology Laboratory UK

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading
data produced by expendable oceanographic profilers/probes and stored in
Lockheed Martin Sippican MK21 Export Data Format (EDF).

PyXPR is released under the MIT license. See the file LICENSE.md for more
information.
"""

import numpy

from .probe import Probe


class XCP(Probe):
    """ Represents an eXpendable Current Profiler (XCP) probe. """

    def read(self, path):
        """ Read and contextualise XCP data.
        :arg str path: The path to the probe's associated EDF file.
        """

        Probe.read(self, path)

        # Check that this data is indeed from an XCP.
        assert(self.type == "XCP")

        # Get the columns of interest and contextualise them.
        self.time = self.data[:, 0].astype(float)
        self.depth = self.data[:, 1].astype(float)
        self.temperature = self.data[:, 2].astype(float)
        self.velocity_ns = self.data[:, 3].astype(float)
        self.velocity_ew = self.data[:, 4].astype(float)
        self.velocity_error = self.data[:, 5].astype(float)

        return
