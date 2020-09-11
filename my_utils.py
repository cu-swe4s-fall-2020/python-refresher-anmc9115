def get_column(file_name, query_column, query_value, result_column=1):
    # open file
    file = open(file_name, 'r')
    # declares array where resuling values will be stored
    results = []
    # skip first line
    next(file)
    
    # reads file
    for line in file:
        columns = line.rstrip().split(',')
        #checking for value in each column of the line
        for i in columns:
            if query_value == columns[query_column]:
                results.append(columns[result_column])
    return results
 