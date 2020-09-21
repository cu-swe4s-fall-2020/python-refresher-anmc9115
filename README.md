# COVID-19 Cases per County
> This project will return an integer array of coronavirus cases recorded in a particular county

The file print_cases takes command line arguments for a csv file containing COVID data 
recieved from https://github.com/nytimes/covid-19-data.git, as well as the county column, 
county of interest, and the cases column. Examples of command line inputs can be found in
run.sh. The print_cases function uses calls upon get_column in my_utils.py in order to
collect and store cases per the specified county in an integer array, which is returned. 

## Installation

OS X & Linux:

```sh
git clone https://github.com/cu-swe4s-fall-2020/python-refresher-anmc9115.git
```

## Usage example
run.sh contains example command line argument inputs
You may run run.sh itself by entering "bash run.sh" into the command line

## Release History

* v1.0
    * ADD: Add `get_column()`
    * ADD: Add `print_cases()`
    * ADD: Add keyword argument for results_column
* v1.1
    * CHANGE: Remove for loop in my_utils
* v2.0
    * ADD: Add command line arguments with argparse
    * CHANGE: `get_column()` returns int array
    * ADD: Add run.sh
    * CHANGE: updated to pep8 style guidelines
    * ADD: Add `main()` in print_cases
