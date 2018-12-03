# PyXPR

PyXPR (Python-based eXpendable Probe Reader) offers functionality for reading data produced by expendable oceanographic profilers/probes and stored in Lockheed Martin Sippican MK21 Export Data Format (EDF).

The following probe types are currently supported, and the code can be readily extended to handle new types:

* eXpendable Bathymetric Thermograph (XBT) probe
* eXpendable Conductivity, Temperature, and Depth (XCTD) probe
* eXpendable Current Profiler (XCP) probe

## Dependencies

In addition to the Python 3.x environment, PyXPR depends on the [NumPy](http://www.numpy.org/) module. This can be installed using the Python package manager `pip`:

```
pip install -r requirements.txt
```

## Installation

Installation can be achieved using Python's [setuptools](https://setuptools.readthedocs.io) module by running:

```
python setup.py install
```

Alternatively, on Linux platforms, add the module to your `PYTHONPATH` environment variable:

```
export PYTHONPATH=$PYTHONPATH:/path/to/pyxpr
```

## Usage
The relevant module for the probe type of interest must first be imported and an object instantiated. The `read` method should then be called with the path to the EDF file provided as an argument. The data for the different fields, such as temperature, will then be stored as attributes.

An example is given below for the case of XCTD probes:

```
from pyxpr.xctd import XCTD

xctd = XCTD()
xctd.read("/path/to/edf_data_file.edf")

print(xctd.temperature)
```

## Authors

* [Christian Thomas Jacobs](http://christianjacobs.uk/)

## Copyright statement

(C) Crown Copyright 2017, 2018 Defence Science and Technology Laboratory UK