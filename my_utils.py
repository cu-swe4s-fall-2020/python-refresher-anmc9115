"""Utilties for reading files

    * get_column - parses a CSV and returns a column
    * get_daily_count - takes a column, returns change each index
    * running_average - returns running avgs over a window throughout list
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
    results_array: integers array
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
            file.close()
            sys.exit(3)
        # checking that results col value exists
        if results_column > len(columns):
            print("You entered results column "
                  + str(results_column)
                  + " but there only "
                  + str(len(columns))
                  + " columns")
            file.close()
            sys.exit(4)

        # adding result col to list that matches query
        if query_value == columns[query_column]:
            # catch type errors
            try:
                results.append(int(columns[results_column]))
            except ValueError:
                print('Column values could not be converted to type int')
                file.close()
                sys.exit(5)

    file.close()

    # convert to array
    results_array = array('i', results)

    return results_array


def get_daily_count(results):
    """Takes an array of cumulative values and computes daily values

    Parameters
    ----------
    results: int array
            an array of cumulative values

    Returns:
    --------
    daily_count: int array
            values of specified column adjusted to daily
            rather than cumulative values
    """

    daily_count = array('i')

    # Fills array with daily count
    for i in range(len(results)):
        if i == 0:
            daily_count.append(results[i])
        else:
            daily_count.append(results[i] - results[i-1])
    return daily_count


def running_average(daily_count, window_size=5):
    """Computes a running average given an array and window.
    
    Parameters
    ----------
    daily_count: int array
            Daily cases or deaths
    window_size: int
            Size of the window (range)

    Returns:
    --------
    running_averages: float list
            List containing the running averages
            for the given window size
    """
    running_avgs = []

    # if window_size too big, adjusted to size of data
    if window_size > len(daily_count):
        window_size = len(daily_count)

    for i in range(len(daily_count)-window_size+1):
        current_window = daily_count[i:i + window_size]
        current_avg = sum(current_window) / window_size
        running_avgs.append(current_avg)

    return (running_avgs, window_size)
