"""Unit testing for functions in my_utils
"""
import my_utils
import unittest
import random
import statistics
import numpy as np
from array import array


class TestGetColumn(unittest.TestCase):

    def test_get_column(self):
        column = my_utils.get_column('test_counties.csv', 1, 'Boulder', 4)
        test_column = array('i', [1, 7, 7, 8, 8, 11, 24, 30, 37, 39, 49,
                                  51, 66, 76, 84, 90, 100, 107, 114, 132])
        self.assertEqual(column, test_column)
        wrong_test_column = array('i', [7, 7, 7, 8, 8, 11, 24, 30,
                                        37, 39, 49, 51, 66, 76, 84,
                                        90, 100, 107, 114, 132])
        self.assertNotEqual(column, wrong_test_column)

    def test_file_not_found(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.get_column('no-data-file.csv', 1, 'Boulder', 4)
        self.assertEqual(cm.exception.code, 1)

    def test_query_col_doesnt_exist(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.get_column('covid-19-data/us-counties.csv', 12,
                                'Boulder', 4)
        self.assertEqual(cm.exception.code, 3)

    def test_result_col_doesnt_exist(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.get_column('covid-19-data/us-counties.csv', 1,
                                'Boulder', 12)
        self.assertEqual(cm.exception.code, 4)

    def test_column_not_int(self):
        with self.assertRaises(SystemExit) as cm:
            my_utils.get_column('covid-19-data/us-counties.csv', 1,
                                'Boulder', 2)
        self.assertEqual(cm.exception.code, 5)


class TestDailyCount(unittest.TestCase):
    def test_daily_count(self):
        # simple test
        column = my_utils.get_column('test_counties.csv', 1, 'Boulder', 4)
        daily = my_utils.get_daily_count(column)
        test_daily = array('i', [1, 6, 0, 1, 0, 3, 13, 6, 7, 2,
                                 10, 2, 15, 10, 8, 6, 10, 7, 7, 18])
        self.assertEqual(daily, test_daily)
        wrong_test_daily = array('i', [7, 7, 7, 8, 8, 11, 24, 30,
                                       37, 39, 49, 51, 66, 76, 84,
                                       90, 100, 107, 114, 132])
        self.assertNotEqual(daily, wrong_test_daily)

        # randomized test
        for i in range(1000):
            data_size = random.randint(100, 1000)
            data = array('i')
            for j in range(data_size):
                data.append(random.randint(1, 100))
            daily = my_utils.get_daily_count(data)
            for k in range(len(daily)):
                if k == 0:
                    self.assertEqual(daily[k], data[k])
                else:
                    self.assertEqual(daily[k], data[k]-data[k-1])

    def test_array_not_numerical(self):
        some_strings = ['a', 'b', 'c', 'd', 'e']
        self.assertRaises(TypeError, my_utils.get_daily_count, some_strings)


class TestRunningAvg(unittest.TestCase):
    def test_running_avg(self):
        # simple test
        avgs, window = my_utils.running_average([4, 6, 3, 1, 8, 99],
                                                window_size=4)
        self.assertEqual(avgs, [3.5, 4.5, 27.75])

        # randomized test
        for i in range(1000):
            data_size = random.randint(100, 1000)
            data = array('i')
            for j in range(data_size):
                data.append(random.randint(1, 100))
            # random window within range
            test_window = data_size - random.randint(1, 100)
            avgs, window_size = my_utils.running_average(data, test_window)
            for j in range(len(avgs)):
                self.assertEqual(avgs[j], np.mean(data[j:j+test_window]))
                self.assertEqual(window_size, test_window)

    def test_window_too_large(self):
        # simple test
        avgs, window = my_utils.running_average([4, 6, 3, 1, 8, 98],
                                                window_size=10)
        self.assertEqual(avgs, [20])
        self.assertEqual(window, 6)

        # randomized test
        for i in range(1000):
            data_size = random.randint(100, 1000)
            data = array('i')
            for j in range(data_size):
                data.append(random.randint(1, 100))
            # window bigger than data size
            test_window = data_size + random.randint(1, 100)
            avgs, window_size = my_utils.running_average(data, test_window)
            for j in range(len(avgs)):
                self.assertEqual(avgs[j], np.mean(data[j:j+data_size]))
                self.assertEqual(window_size, data_size)

    def test_window_negative(self):
        for i in range(1000):
            data_size = random.randint(100, 1000)
            data = array('i')
            for j in range(data_size):
                data.append(random.randint(1, 100))
            # window negative
            test_window = random.randint(-100, -1)
            avgs, window_size = my_utils.running_average(data, test_window)
            for j in range(len(avgs)):
                self.assertEqual(avgs[j], np.mean(data[j:j+5]))
                self.assertEqual(window_size, 5)

    def test_array_not_numerical(self):
        some_strings = ['a', 'b', 'c', 'd', 'e']
        window = random.randint(1, 5)
        self.assertRaises(TypeError, my_utils.running_average,
                          some_strings, window)


if __name__ == '__main__':
    unittest.main()
