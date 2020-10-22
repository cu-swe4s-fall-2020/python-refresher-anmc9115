"""Utilties for reading files

    * get_columns - parses a CSV and returns entered columns
    * get_daily_count - takes a list, returns change each index
    * running_average - returns running avgs over a window throughout list
"""
import sys
import numpy as np
from datetime import datetime
from operator import itemgetter
from array import array
import matplotlib
import matplotlib.pylab as plt
import matplotlib.dates as mdates
matplotlib.use('Agg')


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

    Returns
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
        date_first = True
        try:
            date = columns[0]
            curr_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            date_first = False

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
        if date_first:
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
        if date_first:
            last_date = curr_date

    file.close()

    return results


def get_daily_count(results):
    """Takes an array of cumulative values and computes daily values

    Parameters
    ----------
    results: int list
            a list of cumulative values

    Returns
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

    Returns
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


def binary_search(county_name, counties_pops):
    """Does a binary search for key in the list

    Parameters
    ----------
    county_name: string
            The string to be searched for
    counties_pops: list
            List of lists containing county names and population
            in one state

    Returns
    --------
    county_pop: integer
        Population of the county
    """

    # sorts alphabetically
    counties_pops.sort(key=itemgetter(0))

    # searches for county name and returns pop
    low = -1
    high = len(counties_pops)
    while (high - low > 1):
        mid = (high + low) // 2
        curr_counties_pops = counties_pops[mid]
        curr_county_name = curr_counties_pops[0]
        curr_county_pop = curr_counties_pops[1]
        if county_name == curr_county_name:
            county_pop = curr_county_pop
            return int(county_pop)
        if county_name < curr_county_name:
            high = mid
        else:
            low = mid

    # If not found
    print('Could not find county name')
    return -1


def calc_per_capita(date_cases, county_pop):
    """Calculates per capita values

    Parameters
    ----------
    date_cases: list
            List containg lists of date, cases
    county_pop: int
            Population of a county

    Returns
    --------
    date_percap_cases: list
        List containg lists of date, per-capita cases
    """
    date_percap_cases = []
    date_percap_case = []

    for i in range(len(date_cases)):
        curr_date, case_count = date_cases[i]
        curr_percap = (float(case_count)/county_pop)
        date_percap_case = [curr_date, curr_percap]
        date_percap_cases.append(date_percap_case)

    return date_percap_cases


def plot_lines(points, file_name):
    """Take a list of list of points and plot each list as a line.
        Parameters
        ----------
        points    : list of list of points
                    Each sublist corresponds to the points for one element.
                    Each point has two values, the first will be the X value
                    and the second the Y value
        file_name : string
                    Name of the output file
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    dates = []
    percap = []
    for pairs in points:
        dates.append(pairs[0])
        percap.append(pairs[1])

    ax.set_xticks(dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    ax.plot_date(dates, percap, ls='-', marker=None)
    ax.set_title('COVID-19 Cases Per Capita in Boulder, CO')
    ax.set_ylabel('Cases per Capita')

    # X-axis date labeling
    fig.autofmt_xdate(rotation=90)
    fig.tight_layout()

    plt.savefig(file_name, bbox_inches='tight')
