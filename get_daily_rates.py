import hash_table as ht
import my_utils as mu
import print_cases
import argparse
from datetime import datetime


def get_daily_rates(state, date):
    """Prints daily case rate per capita for a given date

    Parameters
    ----------
    state: string
            Name of state
    date: str
            Date of cases

    Prints/Returns
    --------
    county_names: str list
            Name of the county
    case_rates: float list
            Percap rate for that day
    """
    # initialize hash table
    hcounty_pops = []
    table_size = 1000
    for i in range(table_size):
        hcounty_pops.append([])

    # get counties and pops for a state
    census_name = 'co-est2019-alldata.csv'
    query_column = 5  # state
    query_value = state
    results_columns = [6, 7]
    county_pops = mu.get_columns(census_name,
                                 query_column,
                                 query_value,
                                 results_columns)

    # put counties and pops in a hash table
    for i in range(len(county_pops)):
        if i != 0:  # state name
            curr_county_withc = county_pops[i][0]
            curr_county = curr_county_withc[:-7]
            curr_pop = county_pops[i][1]
            ht.put(hcounty_pops, table_size, curr_county, curr_pop)

    # get cases for each county on date
    case_file = 'covid-19-data/us-counties.csv'
    state_column = 2
    counties_cases = [0, 1, 4]
    date_c_cases = mu.get_columns(case_file,
                                  state_column,
                                  state,
                                  counties_cases)

    # get cases for specific date
    c_cases = []
    for c_date, c_county, c_case in date_c_cases:
        if c_date == date:
            c_cases.append([c_date, c_county, c_case])

    # print county name and percap case rate
    county_names = []
    case_rates = []
    for curr_date, county_name, cases in c_cases:
        county_names.append(county_name)
        c_pop = ht.get(county_name, hcounty_pops, table_size)
        date_case_rate = mu.calc_per_capita([[date, cases]], int(c_pop))
        case_rate = date_case_rate[0][1]
        case_rates.append(case_rate)

        print(county_name, case_rate)

    return county_names, case_rates


def main():
    # Parses through file using command line inputs
    parser = argparse.ArgumentParser(
        description='Gets daily rates')

    parser.add_argument('--state',
                        dest='state',
                        type=str,
                        required=True,
                        help='Enter the name of the state')
    parser.add_argument('--date',
                        dest='date',
                        type=str,
                        required=True,
                        help='Enter date as year-month-day')

    args = parser.parse_args()

    # get daily rates
    get_daily_rates(args.state, args.date)


if __name__ == '__main__':
    main()
