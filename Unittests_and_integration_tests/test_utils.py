#!/usr/bin/env python3
""" Test function access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class TestAccessNestedMap """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    # tester une exeption avec assertRaises
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
