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
import logging


class EDF(object):
    """ A class for handling files in the Lockheed Martin Sippican MK21 Export
    Data Format (EDF). """

    def __init__(self):
        """ Initialise the EDF file handler object. """
        return

    def read(self, path):
        """ Read the header and data from an EDF file.
        :arg str path: The path to the EDF file.
        """

        logging.info("Reading file %s..." % path)
        with open(path, "r") as f:
            self.header = self.read_header(f)
            f.seek(0)  # Go back to the start of the file.
            self.data = self.read_data(f)
        return

    def read_header(self, f):
        """ Read and parse the header of the EDF file.
        :arg f: The open file to read the header from.
        :rtype: dict
        :returns: A dictionary containing header information.
        """

        header = {}

        # Read in relevant header information and skip the rest.
        line = f.readline()
        # NOTE: Some EDF files denote the end of the header by comment lines
        # such as "//Data".
        # However, this may not be the case, so it is assumed here that all
        # data lines are those that contain tab characters.
        while("\t" not in line):

            # Divide up each header line into its name and value.
            try:
                (name, value) = line.split(":", 1)
            except ValueError:
                # Probably a comment line - ignore.
                # Read the next line.
                line = f.readline()
                continue

            # Remove whitespace.
            name = name.strip()
            value = value.strip()

            # Store header information.
            header[name] = value

            # Read the next line.
            line = f.readline()

        return header

    def read_data(self, f):
        """ Read each line of data and split it up into columns.
        :arg f: The open file to read the data from.
        :rtype: numpy.ndarray
        :returns: A 2D array of data.
        """
        data = []
        for line in f:
            if("\t" not in line):
                # This is assumed to be a header line - ignore.
                continue
            data.append(line.split())
        # Convert to a 2D numpy array for better processing.
        # NOTE: Each element of the array is currently a string and may
        # require type casting when processing the data.
        data = numpy.array(data)
        return data
