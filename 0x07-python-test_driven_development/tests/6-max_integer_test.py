#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        n = __import__('6-max_integer').__doc__
        self.assertTrue(len(n) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        n = max_integer.__doc__
        self.assertTrue(len(n) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        n = []
        self.assertIsNone(max_integer(n))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        n = [1]
        self.assertEqual(max_integer(n), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        n = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(n), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        n = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(n), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        n = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(n), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        n = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(n), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        n = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(n)

if __name__ == "__main__":
    unittest.main()
