# runs pycodestyle on files
pycodestyle my_utils.py
pycodestyle print_cases.py
pycodestyle test_my_utils.py

# runs functional test
bash test_print_cases.sh

#runs unit tests
python test_my_utils.py -b
