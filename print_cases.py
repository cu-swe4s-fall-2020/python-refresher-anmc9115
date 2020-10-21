"""Parses file and prints cases

    * print_cases - Prints int array of covid cases for a particular county
    * option to print daily cases and running average
"""
import my_utils as mu
import argparse
import sys
from datetime import datetime


def print_cases(file_name, county_column, county, cases_columns):
    """Calls get_columns() function to return cases for a county.

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

    Prints
    --------
    cases: array of integers
            An array containing all cases for the input county
    """
    cases = mu.get_columns(file_name, county_column, county, cases_columns)
    return cases

# def print_daily_cases()
# def print_running_avg()
# def print_percap_plot
# EG: in main: 
# if print_percap_plot:
#     print_percap_plot()

def main():
    # Parses through file and uses command line for input arguments
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

    # Prints raw cumulative cases in a county
    try:
        county_cases = print_cases(args.file_name,
                                   args.county_column,
                                   args.county,
                                   args.cases_columns)
    except ValueError:
        print('File contains dates that are not sequential')
        sys.exit(6)

    print(*county_cases, sep='\n')

    # Prints daily cases in a county
    daily_count = mu.get_daily_count(county_cases)
    if args.print_daily_cases:
        print(*daily_count, sep='\n')

    # Prints running avg for a county
    if args.print_running_avg:
        try:
            running_avg, window = mu.running_average(daily_count,
                                                     args.window_size)
        except TypeError:
            running_avg, window = mu.running_average(daily_count)
        print(*running_avg, sep='\n')
        print(window)
        
    # Prints plot of per-capita case data for a county
    if args.print_percap_plot:
        # Get dates and cases
        county_column = 1
        dates_cases_columns = [0,4]
        date_cases = mu.get_columns(args.file_name,
                                    county_column,
                                    args.county,
                                    dates_cases_columns)

        # Get population of the county
        state_column = 5
        state = 'Colorado'
        counties_pops = mu.get_columns('co-est2019-alldata.csv',
                                       state_column,
                                       state,
                                       [6,7])

        county_pop = mu.binary_search('Boulder County', counties_pops)

        # Calculate Per Capita Rates
        date_percap = mu.calc_per_capita(date_cases, county_pop) 
        plot_points = []
        for i in range(len(date_percap)):
            curr_date = (date_percap[i])[0]
            date = datetime.strptime(curr_date, '%Y-%m-%d')
            plot_points.append([date, (date_percap[i])[1]])
        
        # Plot
        mu.plot_lines(plot_points, ['Dates', 'Per-Capita Cases'], 'percap_cases_boulder.png')
        

if __name__ == '__main__':
    main()
