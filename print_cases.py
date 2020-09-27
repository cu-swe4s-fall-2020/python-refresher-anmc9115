"""Parses file and prints cases

    * print_cases - Prints int array of covid cases for a particular county
    * option to print daily cases and running average
"""
import my_utils as mu
import argparse


def print_cases(file_name, county_column, county, cases_column):
    """Calls get_column() function to return cases for a county.

    Parameters
    ----------
    file_name: string
            The path to the CSV file
    county_column: integer
            The column containing the county strings
    county: string
            The name of the county
    cases_column: integer
            The column containing the case data

    Returns:
    --------
    cases: array of integers
            An array containing all cases for the input county
    """
    cases = mu.get_column(file_name, county_column, county, cases_column)
    return cases


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
    parser.add_argument('--cases_column',
                        dest='cases_column',
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

    args = parser.parse_args()

    county_cases = print_cases(args.file_name,
                               args.county_column,
                               args.county,
                               args.cases_column)

    print(*county_cases, sep='\n')

    daily_count = mu.get_daily_count(args.file_name,
                                     args.county_column,
                                     args.county,
                                     args.cases_column)
    if args.print_daily_cases:
        print(*daily_count, sep='\n')

    if args.print_running_avg:
        try:
            running_avg = mu.running_average(daily_count,
                                             args.window_size)
        except TypeError:
            running_avg = mu.running_average(daily_count)
        
        print(*running_avg, sep='\n')


if __name__ == '__main__':
    main()
