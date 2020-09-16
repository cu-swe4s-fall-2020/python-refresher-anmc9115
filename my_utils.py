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
        # adding each value from the result column which
        # has a value in query col that matches the query value
        if query_value == columns[query_column]:
            results.append(columns[result_column])
    
    # close file
    file.close()
    
    return results
 
    
print(get_column('covid-19-data/us-counties.csv',1,'Boulder',4))