# encoding: utf-8
import unittest

from sort.quick_sort import sort


class TestDivide(unittest.TestCase):

    def test_count(self):
        order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        o1 = [1, 2, 4, 5, 6, 7, 8, 9, 3]
        sort(o1)
        self.assertEqual(order, o1)

        o2 = [9, 4, 5, 1, 7, 8, 2, 3, 6, ]
        sort(o2)
        self.assertEqual(order, o2)


if __name__ == '__main__':
    unittest.main()
