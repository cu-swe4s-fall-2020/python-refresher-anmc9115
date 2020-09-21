from array import array

def get_column(file_name, query_column, query_value, results_column):
    # open file
    file = open(file_name, 'r')
    
    # declares array where resuling values will be stored
    results = []
    
    # skip first line
    next(file)
    
    # reads file
    for line in file:
        columns = line.rstrip().split(',')
        # adding each value from the result column which
        # has a value in query col that matches the query value
        if query_value == columns[query_column]:
            results.append(int(columns[results_column]))
    
    # close file
    file.close()
    
    results_array = array('i',results)
    
    return results_array
