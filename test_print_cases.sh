test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Test correct input
run test_print_cases python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132'

# Test file not found
run test_file_not_found python print_cases.py --file fileDNE.csv --county_column 1 --county 'Boulder' --cases_column 4
assert_exit_code 1
assert_in_stdout 'Could not find file: fileDNE.csv'

# Test permission error
run test_file_not_accessible python print_cases.py --file private_test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4
assert_exit_code 2
assert_in_stdout 'Could not access file: private_test_counties.csv'

# Test query column DNE
run test_query_doesnt_exist python print_cases.py --file test_counties.csv --county_column 12 --county 'Boulder' --cases_column 4
assert_exit_code 3
assert_in_stdout 'You entered query column 12 but there are only 7 columns'

# Test result column DNE
run test_result_doesnt_exist python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 12
assert_exit_code 4
assert_in_stdout 'You entered results column 12 but there only 7 columns'

# Test result column not numerical
run test_result_not_numeric python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 2
assert_exit_code 5
assert_in_stdout 'Column values could not be converted to type int'

# Test print daily cases
run test_print_daily python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4 --print_daily_cases 1
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132
1
6
0
1
0
3
13
6
7
2
10
2
15
10
8
6
10
7
7
18'

# Test print running avg w/o specified window size
run test_print_running_avg python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4 --print_running_avg 1
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132
1.6
2.0
3.4
4.6
5.8
6.2
7.6
5.4
7.2
7.8
9.0
8.2
9.8
8.2
7.6
9.6
5'

# Test running_avg with window in range
run test_window_in_range python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4 --print_running_avg 1 --window_size 10
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132
3.9
4.8
4.4
5.9
6.8
7.6
7.9
7.6
7.7
7.7
9.3
10'

# Test running_avg with window out of range
run test_window_out_of_range python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4 --print_running_avg 1 --window_size 25
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132
6.6
20'

# Test negative window size
run test_negative_window python print_cases.py --file test_counties.csv --county_column 1 --county 'Boulder' --cases_column 4 --print_running_avg 1 --window_size -5
assert_exit_code 0
assert_in_stdout '1
7
7
8
8
11
24
30
37
39
49
51
66
76
84
90
100
107
114
132
1.6
2.0
3.4
4.6
5.8
6.2
7.6
5.4
7.2
7.8
9.0
8.2
9.8
8.2
7.6
9.6
5'