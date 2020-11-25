''' Hash table implementation

    * ascii_hash_function - takes a string and table size and
      returns hash value
    * put - add a value to the table by hash_string
    * get - get a value from the table by hash_string
'''


def ascii_hash_function(hash_string, table_size):
    """Takes table size and string and returns ascii hash value

    Parameters
    ----------
    table_size: int
            size of the hash table
    hash_string: string
            string to determine hash value for
    Returns
    --------
    hash_val: int
            hash value produced for hash_string
    """
    s = 0
    for i in range(len(hash_string)):
        s += ord(hash_string[i])

    hash_val = s % table_size

    return hash_val


def put(hash_table, table_size, hash_string, value):
    """Adds a value to the hash table by hash_string

    Parameters
    ----------
    hash_table: array
            Hash table holding values
    hash_string: string
            Value to be added to the hash table
    table_size: int
            Size of hash table
    value: any
            Paired with hash_string
    Returns
    --------
    hash_table: array
            returns table with added hash_string
    """
    # gets hash value
    hash_val = ascii_hash_function(hash_string, table_size)

    # puts in hash table
    hash_table[hash_val].append((hash_string, value))
    return True


def get(query_string, hash_table, table_size):
    """Adds a value to the hash table by hash_string

    Parameters
    ----------
    query_string: string
            Key to search for
    hash_table: array
            Hash table holding values
    table_size: int
            Size of the hash table
    Returns
    --------
    value: any
            Returns val associated with query string
    """
    # get hash value to search for
    hash_val = ascii_hash_function(query_string, table_size)

    # search table for hash val, return value
    for hash_string, value in hash_table[hash_val]:
        if query_string == hash_string:
            return value

    return None
