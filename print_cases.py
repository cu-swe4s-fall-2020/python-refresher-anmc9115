import my_utils as mu

county='Boulder'
county_column = 1
file_name = 'covid-19-data/us-counties.csv'
cases = mu.get_column(file_name,county_column,county,result_column=4)
print(cases)
