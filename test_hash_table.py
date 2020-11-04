"""Unit testing for functions in hash_table
"""
import hash_table
import unittest


class TestHashTable(unittest.TestCase):

    def test_ascii_test_hash_function(self):
        val = hash_table.ascii_hash_function('hello', 500)
        hello_hash = (104+101+108+108+111) % 500
        self.assertEqual(val, hello_hash)

    def test_put(self):
        htable = []
        for i in range(500):
            htable.append([])
        hash_table.put(htable, 500, 'testmystring', 8002334)

        hash_val = hash_table.ascii_hash_function('testmystring', 500)
        self.assertEqual(htable[hash_val][0][0], 'testmystring')
        self.assertEqual(htable[hash_val][0][1], 8002334)

    def test_get(self):
        htable = []
        for i in range(500):
            htable.append([])
        hash_table.put(htable, 500, 'testmystring', 8002334)
        val = hash_table.get('testmystring', htable, 500)
        val0 = hash_table.get('notmystring', htable, 500)
        self.assertEqual(val, 8002334)
        self.assertEqual(val0, None)


if __name__ == '__main__':
    unittest.main()
