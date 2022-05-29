# Command Line Interface Data Visualization (graphing)

The purpose of this project is to demonstrate how data can be visuaized in the command line interface

The tool fetches data from an endpoint, converts the data to python dictionary and then plots it.

## Setup/Installation
**Warning:** Python, pip and git needs to be installed on your machine and they have to be added to the *PATH* environment variable, to allow execution from Command Line Interface (CLI).

First clone the project to your local machine.
A script has been written to automatically setup the project.
Navigate to the project's root directory and execute the command below to setup the project

*For Windows*
```shell
scripts\setup.bat
```
*For Linux*
```shell
bash scripts/setup.sh
```
*Note:* Your internet connection must be ON for this command to execute successfully

The command above performs the following actions:
- installs Virtual environment wrapper
- creates the virtual environment for the project
- activates the virtual environment
- installs the project requirements, including a code linter, code formatter and a pre-commit hook manager
- installs pre-commit hook

## Usage
If the virtual environment is not already activated, then execute the following command to activate the virtual environment.

```shell
workon cli-grapher
```
*Note:* cli-grapher is the virtual environment created during setup

Once the virtual environment is active, navigate to the project root directory and execute the grapher command to test the implementation.

It takes 2 args, *start_data* and *end_date* all in the format *dd-mm-yy*.
Example:

```shell
python grapher 01-01-2022 12-01-2022
```
Then watch it draw the bar graph of the data.

## Optimization
A naive cache implementation optimizes the fetching of the data.

The filtering algorithm used, leverages *Binary Search* algorithm to find the starting and ending indexes of data to return to the user. The algorithm is a modified version of binary search.
Since the algorithm is binary search based, it's worst case time complexity is O(logN) or logarithmic time, which is well optimized. The space complexity is constant since the algorithm does not create new data during the search for the indexes.

## Quality Assurance

The code linter, code formatter and automated testing which tested several corner cases ensures the quality of the code.
