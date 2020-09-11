def get_column(file_name, query_column, query_value, result_column):
    # opening file, addressing header
    file = open(file_name, 'r')
    header = None
    # declares array where resuling values will be stored
    results = []
    for line in file:
        if header == None:
            line = header
            continue
        # Reading lines 
        columns = line.rstrip.split(',')
        # checking for value in each column of the line
        for i in columns:
            if query_value == query_column[i]:
                results.append(columns[result_column])
    return results
 