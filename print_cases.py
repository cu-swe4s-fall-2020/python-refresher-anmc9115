import my_utils as mu
import argparse

def print_cases(file_name, county_column, county, cases_column):
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

    args = parser.parse_args()
    
    county_cases = print_cases(args.file_name, args.county_column, args.county, args.cases_column)
    
    print(county_cases)
    
if __name__ == '__main__':
    main()