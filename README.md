# COVID-19 Cases per County
> This project will print cumulative, daily, and a running average of cases recorded in a county

The file print_cases takes command line arguments for a csv file containing COVID data 
recieved from https://github.com/nytimes/covid-19-data.git, as well as the county column, 
county of interest, and the cases column. The print_cases function calls upon get_column 
in my_utils.py in order to collect and store cases per the specified county in an integer 
array, which is returned. There are options to print the daily cases, rather than cumulative
cases, as well as the running average over a given window. Files which contain skipped days 
will be filled in, and those which contain out-of order dates will raise an error. 

## Installation

OS X & Linux:

```sh
git clone https://github.com/cu-swe4s-fall-2020/python-refresher-anmc9115.git
```

## Usage example
`test_print_cases.sh` contains test arguments that are formatted for command line inputs
`run.sh` runs `test_print_cases.sh` and may be run itself with the command: bash run.sh

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
* v3.0
    * ADD: `get_daily_count()` in my_utils
    * ADD: `running_average()` in my_utils
    * ADD: `test_my_utils.py` unit tests for my_utils
    * ADD: `test_print_cases.sh` functional test for print_cases
    * CHANGE: update formatting in my_utils and print_cases
* v3.1
   * CHANGE: added missing for loop in random data generation for `test_my_utils.py`
* v4.0
   * ADD: skipped days are filled in in `get_column()` of `my_utils.py`
   * ADD: out of order days raise a ValueError in `get_column()` of `my_utils.py`
   * CHANGE: functional and unit tests updated
   * CHANGE: continuous integration implemented using `.travis.yml`
