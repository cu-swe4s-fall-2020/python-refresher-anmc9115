"""Parses file and prints cases

    * print_cases - Prints int array of covid cases for a particular county
    * option to print daily cases and running average
"""
import my_utils as mu
import argparse
import sys
from datetime import datetime


def print_cases(file_name, county_column, county, cases_columns):
    """Calls get_columns() function to return cases for a county

    Parameters
    ----------
    file_name: string
            The path to the CSV file
    county_column: integer
            The column containing the county strings
    county: string
            The name of the county
    cases_columns: list of lists
            Containing the resulting columns

    Prints/Returns
    --------
    cases: array of integers
            An array containing all cases for the input county
    """
    try:
        cases = mu.get_columns(file_name, county_column, county, cases_columns)
        print(*cases, sep='\n')
    except ValueError:
        print('File contains dates that are not sequential')
        sys.exit(6)
    return cases


def print_daily_cases(county_cases):
    """Calls get_daily_count() function and prints daily counts

    Parameters
    ----------
    county_cases: list
            List of cases in a county

    Prints
    --------
    daily_count: list
            List of daily counts in a county

    """
    daily_count = mu.get_daily_count(county_cases)
    print(*daily_count, sep='\n')


def print_running_avg(daily_cases, window_size):
    """Calls running_average() and prints running avg
       and window size

    Parameters
    ----------
    daily_cases: list
            List of daily counts in a county
    window_size: int
            Size of window to use in calculation

    Prints
    --------
    running_avg: list of floats
            Running averages for daily counts
    window: int
            Size of the window used in calculation
    """
    try:
        running_avg, window = mu.running_average(daily_cases,
                                                 window_size)
    except TypeError:
        running_avg, window = mu.running_average(daily_cases)
    print(*running_avg, sep='\n')
    print(window)


def print_percap_plot(file_name, county):
    """Calls plot_lines() and outputs png plot

    Parameters
    ----------
    file_name: string
            Name of case data file
    county: string
            Name of county

    Outputs
    --------
    percap_cases_boulder.png: png file
            Graph of per capita covid cases in a county
    """
    # Get dates and cases
    county_column = 1
    dates_cases_columns = [0, 4]
    date_cases = mu.get_columns(file_name,
                                county_column,
                                county,
                                dates_cases_columns)

    # Get population of the county
    state_column = 5
    state = 'Colorado'
    counties_pops = mu.get_columns('co-est2019-alldata.csv',
                                   state_column,
                                   state,
                                   [6, 7])

    county_pop = mu.binary_search('Boulder County', counties_pops)

    # Calculate Per Capita Rates
    date_percap = mu.calc_per_capita(date_cases, county_pop)
    plot_points = []
    for i in range(len(date_percap)):
        curr_date = (date_percap[i])[0]
        date = datetime.strptime(curr_date, '%Y-%m-%d')
        plot_points.append([date, (date_percap[i])[1]])

    # Plot
    mu.plot_lines(plot_points, 'percap_cases_boulder.png')


def main():
    # Parses through file using command line inputs
    parser = argparse.ArgumentParser(
        description='Returns a column from a file')

    parser.add_argument('--file',
                        dest='file_name',
                        type=str,
                        required=True,
                        help='Enter file name to be parsed.')
    parser.add_argument('--county_column',
                        dest='county_column',
                        type=int,
                        required=True,
                        help='Enter the column containing county strings')
    parser.add_argument('--county',
                        dest='county',
                        type=str,
                        required=True,
                        help='Enter the county string')
    parser.add_argument('--cases_columns',
                        dest='cases_columns',
                        nargs='+',
                        type=int,
                        required=True,
                        help='Enter the cases column to be returned')
    parser.add_argument('--print_daily_cases',
                        dest='print_daily_cases',
                        type=bool,
                        required=False,
                        help='Enter 1 to print daily cases')
    parser.add_argument('--print_running_avg',
                        dest='print_running_avg',
                        type=bool,
                        required=False,
                        help='Enter 1 to print running avg')
    parser.add_argument('--window_size',
                        dest='window_size',
                        type=int,
                        required=False,
                        help='Enter window size for avg calculation')
    parser.add_argument('--print_percap_plot',
                        dest='print_percap_plot',
                        type=bool,
                        required=False,
                        help='Enter 1 to print per capita plot')

    args = parser.parse_args()

    # Print Cases
    county_cases = print_cases(args.file_name, args.county_column,
                               args.county, args.cases_columns)

    # Print Daily Cases
    if args.print_daily_cases:
        print_daily_cases(county_cases)

    # Print Running Average
    if args.print_running_avg:
        daily_cases = mu.get_daily_count(county_cases)
        print_running_avg(daily_cases, args.window_size)

    # Print Percapita Plot
    if args.print_percap_plot:
        print_percap_plot(args.file_name, args.county)


if __name__ == '__main__':
    main()
