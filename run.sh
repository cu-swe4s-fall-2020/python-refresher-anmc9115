# runs pycodestyle on files
pycodestyle my_utils.py
pycodestyle print_cases.py
pycodestyle test_my_utils.py
pycodestyle get_daily_rates.py
pycodestyle test_hash_table.py
pycodestyle hash_table.py

# runs functional test
bash test_print_cases.sh
bash test_get_daily_rates.sh

#runs unit tests
python test_my_utils.py -b
python test_hash_table.py