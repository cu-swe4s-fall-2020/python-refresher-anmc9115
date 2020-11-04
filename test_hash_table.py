"""Unit testing for functions in hash_table
"""
import hash_table
import unittest
import random

class TestHashTable(unittest.TestCase):
    
    def ascii_test_hash_function(self):
        val = hash_table.hash_function('hello', 5)
        self.assertEqual(val, 2)
    
    def test_put(self):
        htable = []
        hash_table.put(htable, 'hello')
        hash_table.put(htable, 'there')
        hellohash = hash_table.hash_function('hello')
        therehash = hash_table.hash_function('there')
        print(htable)
        
#     def test_get(self):
    
        
    
if __name__ == '__main__':
    unittest.main()