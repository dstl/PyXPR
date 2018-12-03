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


class XCTD(Probe):
    """ Represents an eXpendable Conductivity, Temperature, and Depth (XCTD)
    probe. """

    def read(self, path):
        """ Read and contextualise XCTD data.
        :arg str path: The path to the probe's associated EDF file.
        """

        Probe.read(self, path)

        # Check that this data is indeed from an XCTD.
        assert(self.type == "XCTD-1")

        # Get the columns of interest and contextualise them.
        self.time = self.data[:, 0].astype(float)
        self.depth = self.data[:, 2].astype(float)
        self.temperature = self.data[:, 3].astype(float)
        self.conductivity = self.data[:, 4].astype(float)
        self.salinity = self.data[:, 5].astype(float)
        self.density = self.data[:, 7].astype(float)
        self.status = self.data[:, 8].astype(int)

        return

    def filter(self, data):
        """ Extract only those data measurements that were recorded when the
        probe status was ok (assumed to be Status Code 8000).
        :arg numpy.array data: The array of data values to be filtered.
        :rtype: numpy.array
        :returns: A new array containing only the data values that were
        recorded when the probe status was ok.
        """

        filtered = []
        for i in range(len(self.status)):
            if (self.status[i] != 8000):
                # Ignore invalid measurement.
                continue
            else:
                filtered.append(data[i])
        return numpy.array(filtered)
