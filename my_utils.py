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
