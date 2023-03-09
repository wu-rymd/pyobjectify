# pyobjectify

Bridge the gap across the different file formats and streamline the process to accessing ingested data via Python objects

![license](https://img.shields.io/badge/license-MIT-green?style=flat-square&color=022169) ![issues](https://img.shields.io/github/issues/wu-rymd/pyobjectify?style=flat-square&color=841C1C) [![codecov](https://codecov.io/gh/wu-rymd/pyobjectify/branch/main/graph/badge.svg?token=410L0PN9UC)](https://codecov.io/gh/wu-rymd/pyobjectify) ![build](https://img.shields.io/github/actions/workflow/status/wu-rymd/pyobjectify/build.yml)

## Overview

Open data is abound. For example, NYC Open Data has over 3,000 datasets spanning over 97 agencies in New York City. This data comes in many different formats, including CSV, JSON, XML, XLS/XLSX, KML, KMZ, Shapefile, GeoJSON, JSON, and more.

In order to import and analyze the data in Python involves sending a request to download the raw data, then converting it into a Python object so that methods can be used to parse its contents. However, this process varies across the many different data types.

This project aims to streamline this process and bridge the gap across the different file formats to allow the end user to get started on data analytics more quickly with a quick function call.

## Development

This project uses a `Makefile` as a command registry, with the following commands:

- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution
