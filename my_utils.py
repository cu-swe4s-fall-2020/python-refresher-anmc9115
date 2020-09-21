from array import array
import sys

def get_column(file_name, query_column, query_value, results_column):
    # open file, catch errors
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("Could not find file: " + file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not access file: " + file_name)
        sys.exit(2)
    
    # skip first line
    next(file)
    
    # reads file
    results = []
    for line in file:
        columns = line.rstrip().split(',')
        
        # checking that query col value exists
        if query_column > len(columns):
            print("You entered query column " \
                  + str(query_column) \
                  + " but there are only " \
                  + str(len(columns)) \
                  + " columns")
            sys.exit(3)
        # checking that results col value exists
        if results_column > len(columns):
            print("You entered results column " \
                  + str(results_column) \
                  + " but there only " \
                  + str(len(columns)) \
                  + " columns")
            sys.exit(4)
            
        # adding result col to list that matches query
        if query_value == columns[query_column]:
            # catch type errors
            try:
                results.append(int(columns[results_column]))
            except:
                print('Column values could not be converted to type int')
                sys.exit(5)
    
    file.close()
    
    # convert to array
    results_array = array('i',results)
    
    return results_array
