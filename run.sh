# this one works
python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --county 'Boulder' --cases_column 4

# this one gives a file not found error
python print_cases.py --file covid-data/us-counties.csv --county_column 1 --county 'Boulder' --cases_column 4

# this one gives a nonexistant column error 
python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --county 'Boulder' --cases_column 12