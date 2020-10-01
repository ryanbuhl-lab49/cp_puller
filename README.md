Coderpad puller
===
`cp_pull` is a simple script for pulling all candidate pads from [Coderpad](https://coderpad.io) for archival purposes.

## Features
- Written in Python
- Small, simple options list
- Short dependency list

## Requirements
- Python 3.7.1+

## Installation for development
1. clone the repo using:  
`git clone git@github.com:ryanbuhl-lab49/cp_puller.git`
2. change into the `cp-puller` directory  
`cd cp_puller`  
3. create a virtual environment:  
`python -m venv .cp-puller-venv`
4. activate the virtual environemnt
`. .cp_puller-venv/bin/activate` on *nix platforms or  
`.cp_puller-venv\Scripts\activate` on Windows platforms
5. install the dependencies with `pip` using:
`pip install --editable .`

## Installation for use
1. clone the repo using:  
`git clone git@github.com:ryanbuhl-lab49/cp_puller.git`
2. change into the `cp_puller` directory
`cd cp_puller`  
3. create a virtual environment (Optional but recommended)  
`python -m venv .cp_puller-venv`
4. activate the virtual environemnt (only if a virtual environment was created)
`. .cp_puller-venv/bin/activate` on *nix platforms or  
`.cp_puller-venv\Scripts\activate` on Windows platforms
5. install the script and dependencies with `pip` using:
`pip install .`

## Usage
    Usage: cp_pull [OPTIONS] KEY

    Script to pull pads from Coderpad using the API token provided

    KEY: Coderpad API key to use

    Options:
      --file TEXT  Name of the file to dump the pads information into
      --help       Show this message and exit.
