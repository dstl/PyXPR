#!/usr/bin/env python

"""
(C) Crown Copyright 2017, 2018 Defence Science and Technology Laboratory UK

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading
data produced by expendable oceanographic profilers/probes and stored in
Lockheed Martin Sippican MK21 Export Data Format (EDF).

PyXPR is released under the MIT license. See the file LICENSE.md for more
information.
"""

import re
from datetime import datetime
import logging

from .edf import EDF


class Probe(EDF):
    """ The base class for a probe. """

    def read(self, path):
        """ Initialise the probe object by reading and parsing its data and metadata.
        :arg str path: The path to the probe's associated EDF file.
        """

        EDF.read(self, path)
        self.parse_metadata(self.header)
        return

    def parse_metadata(self, header):
        """ Process the relevant probe metadata in the header and store it as
        class attributes.
        :arg dict header: The dictionary containing header entries.
        """

        # Probe Type.
        try:
            self.type = header["Probe Type"]
        except Exception as error:
            logging.error("Probe Type could not be parsed.")
            logging.exception(error)
            self.type = None

        # Date/Time of Launch.
        try:
            date = datetime.strptime(header["Date of Launch"], "%m/%d/%Y")
            time = datetime.strptime(header["Time of Launch"], "%H:%M:%S")
            # Combine launch date and time.
            self.launch = datetime(date.year, date.month, date.day, time.hour,
                                   time.minute, time.second)
        except Exception as error:
            logging.error("""Date of Launch and/or Time of Launch could not be
                          parsed.""")
            logging.exception(error)
            self.launch = None

        # Sequence Number.
        try:
            self.sequence_number = int(header["Sequence Number"])
        except Exception as error:
            logging.error("Sequence Number could not be parsed.")
            logging.exception(error)
            self.sequence_number = None

        # Latitude and Longitude.
        try:
            self.latitude = self.parse_latitude_longitude(header["Latitude"])
            self.longitude = self.parse_latitude_longitude(header["Longitude"])
        except Exception as error:
            logging.error("Latitude and/or Longitude could not be parsed.")
            logging.exception(error)
            self.latitude = None
            self.longitude = None

        return

    def parse_latitude_longitude(self, latitude_longitude):
        """ Parse latitude or longitude strings and convert to decimal degrees.
        :arg str latitude_longitude: The string of latitude or longitude
        coordinates to parse.
        :rtype: float
        :return: The latitude or longitude value in decimal degrees.
        """

        pattern = re.compile("(\d+) (\d+.?\d*)([N,S,E,W])")
        match = pattern.match(latitude_longitude)

        degrees = float(match.group(1))
        decimal_minutes = float(match.group(2))
        direction = match.group(3)  # N, S, E, W.

        # Convert from degrees decimal minutes format to decimal degrees.
        decimal_degrees = degrees + decimal_minutes/60.0
        if(direction == "S" or direction == "W"):
            decimal_degrees = -decimal_degrees
        return decimal_degrees
