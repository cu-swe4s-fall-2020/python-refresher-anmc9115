import my_utils as mu

county='Boulder'
county_column = 1
cases_column = 4
file_name = 'covid-19-data/us-counties.csv'
cases = mu.get_column(file_name,county_column,county,cases_column)
print(cases)
