# encoding: utf-8
import unittest

from hello_world.count import count


class TestDivide(unittest.TestCase):
    def test_count(self):
        self.assertEqual(2, count((1, 2)))
        self.assertEqual(3, count([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
