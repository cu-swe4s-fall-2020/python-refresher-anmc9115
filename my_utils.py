"""Utilties for reading files

    * get_columns - parses a CSV and returns a column
    * get_daily_count - takes a column, returns change each index
    * running_average - returns running avgs over a window throughout list
"""
from array import array
import sys
from datetime import datetime


def get_columns(file_name, query_column, query_value, results_columns):
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
    results_columns: list of ints
            The columns containing values to be collected

    Returns:
    --------
    results_array: integers array
           values collected from results_columns based on query inputs
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
    last_date = None
    for line in file:
        columns = line.rstrip().split(',')
        date = columns[0]
        curr_date = datetime.strptime(date, '%Y-%m-%d')

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
        for i in range(len(results_columns)):
            if results_columns[i] > len(columns):
                print("You entered results column "
                      + str(results_columns)
                      + " but there only "
                      + str(len(columns))
                      + " columns")
                file.close()
                sys.exit(4)

        # filling cases between skipped dates
        if last_date is not None:
            delta = curr_date - last_date
            if delta.days > 1:
                for i in range(delta.days - 1):
                    results.append(results[-1])
            if delta.days < 1:
                raise ValueError

        # adding result col to list that matches query
        if query_value == columns[query_column]:
            if columns[query_column] == query_value:
                result = []
                for result_column in results_columns:
                    result.append(columns[result_column])
                results.append(result)
        last_date = curr_date

    file.close()

    return results


def get_daily_count(results):
    """Takes an array of cumulative values and computes daily values

    Parameters
    ----------
    results: int list
            a list of cumulative values

    Returns:
    --------
    daily_count: int array
            values of specified column adjusted to daily
            rather than cumulative values
    """

    flat_results = []

    # converts list of lists to flat int list
    for sublist in results:
        for item in sublist:
            flat_results.append(int(item))

    daily_count = []

    # Fills array with daily count
    for i in range(len(flat_results)):
        if i == 0:
            daily_count.append(flat_results[i])
        else:
            daily_count.append(flat_results[i] - flat_results[i-1])
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
    # if window_size negative, restore to default
    if window_size < 0:
        window_size = 5

    for i in range(len(daily_count)-window_size+1):
        current_window = daily_count[i:i + window_size]
        current_avg = sum(current_window) / window_size
        running_avgs.append(current_avg)

    return (running_avgs, window_size)
