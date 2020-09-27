"""Utilties for reading files

    * get_column - parses a CSV and returns a column
"""
from array import array
import sys


def get_column(file_name, query_column, query_value, results_column):
    """Opens a csv and returns a column as an array of integers.

    Parameters
    ----------
    file_name: string
            The path to the CSV file
    query_column: integer
            The column containing the query string
    query_value: string
            For each occurance of this string, values from the
            results column of the same row will be collected
    results_column: integer
            The column containing values to be collected

    Returns:
    --------
    results_array: array of integers
           values collected from results_column based on query inputs
    """
    # open file, catch errors
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("Could not find file: " + file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not access file: " + file_name)
        sys.exit(2)

    # skip first line
    next(file)

    # reads file
    results = []
    for line in file:
        columns = line.rstrip().split(',')

        # checking that query col value exists
        if query_column > len(columns):
            print("You entered query column "
                  + str(query_column)
                  + " but there are only "
                  + str(len(columns))
                  + " columns")
            sys.exit(3)
        # checking that results col value exists
        if results_column > len(columns):
            print("You entered results column "
                  + str(results_column)
                  + " but there only "
                  + str(len(columns))
                  + " columns")
            sys.exit(4)

        # adding result col to list that matches query
        if query_value == columns[query_column]:
            # catch type errors
            try:
                results.append(int(columns[results_column]))
            except ValueError:
                print('Column values could not be converted to type int')
                sys.exit(5)

    file.close()

    # convert to array
    results_array = array('i', results)

    return results_array


def get_daily_count(file_name, query_column, query_value, results_column):
    """Opens a csv and

    Parameters
    ----------
    file_name: string
            The path to the CSV file
    query_column: integer
            The column containing the query string
    query_value: string
            For each occurance of this string, values from the
            results column of the same row will be collected
    results_column: integer
            The column containing values to be collected

    Returns:
    --------
    daily_count: int array
            values of specified column adjusted to daily
            rather than cumulative values
    """

    # Runs get_column to recieve array value
    results = get_column(file_name, query_column, query_value, results_column)
    daily_count = array('i')

    # Fills array with daily count
    for i in range(len(results)):
        if i == 0:
            daily_count.append(results[i])
        else:
            daily_count.append(results[i] - results[i-1])
    return daily_count


def running_average(daily_count, window_size=5):
    """Opens a csv and

    Parameters
    ----------
    daily_cases: int array
            Daily cases or deaths
    window_size: int
            Size of the window (range)

    Returns:
    --------
    running_averages: float array
            Array containing the running average
            for the given window size
    """
    # open file, catch errors
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("Could not find file: " + file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not access file: " + file_name)
        sys.exit(2)

    # skip first line
    next(file)

    return daily_numbers
