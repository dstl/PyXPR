#!/usr/bin/env python

"""
(C) Crown Copyright 2017, 2018 Defence Science and Technology Laboratory UK

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading
data produced by expendable oceanographic profilers/probes and stored in
Lockheed Martin Sippican MK21 Export Data Format (EDF).

PyXPR is released under the MIT license. See the file LICENSE.md for more
information.
"""

from distutils.core import setup


setup(name="PyXPR",
      version="1.0.0",
      description="""PyXPR (Python-based eXpendable Probe Reader) offers
                   functionality for reading data produced by expendable
                   oceanographic profilers/probes and stored in Lockheed
                   Martin Sippican MK21 Export Data Format (EDF).""",
      author="Christian Thomas Jacobs",
      author_email="cjacobs@dstl.gov.uk",
      packages=["pyxpr"],
      classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
      ]
      )
